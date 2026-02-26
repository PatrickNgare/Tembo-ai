"""
rag.py
RAG pipeline for Tembo AI.

Stack (100% free):
  - sentence-transformers  → local embeddings, no API quota
  - PostgreSQL + pgvector  → vector storage & semantic search
  - Groq API               → fast, free LLM (Llama 3.3 70B)
"""

import os
from typing import Optional
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

from vector_store import similarity_search, get_history, save_message

load_dotenv()

# ── Groq client ─────────────────────────────────────────────────────────────────
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Groq free models (pick one):
#   llama-3.3-70b-versatile   ← best quality, still fast
#   llama3-8b-8192            ← fastest, great for demos
#   mixtral-8x7b-32768        ← large context window
MODEL = "llama-3.3-70b-versatile"

# ── System prompt ────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are Tembo, an expert AI travel assistant for Kenya.
You help tourists plan trips, find destinations, understand costs, and get travel advice.

RULES:
- Answer ONLY based on the CONTEXT provided. Do not invent facts.
- Always include prices in both KES and USD when available.
- If the context lacks enough information, say so honestly.
- Be warm and friendly. Use occasional Swahili: Karibu (welcome), Asante (thank you), Hakuna Matata (no worries).
- Keep answers practical and well structured.
"""


# ── Core RAG function ─────────────────────────────────────────────────────────────
def rag_answer(
    question: str,
    session_id: Optional[str] = None,
    top_k: int = 5,
    category_filter: Optional[str] = None,
) -> dict:
    """
    Full RAG pipeline:
      1. Embed query locally  →  free, instant
      2. Search pgvector      →  top_k relevant chunks
      3. Load chat history    →  for conversational context
      4. Call Groq LLM        →  generate grounded answer
      5. Save to history
      6. Return answer + sources
    """

    # Normalize "null" string to None
    if category_filter in (None, "null", "None", ""):
        category_filter = None

    # ── 1 & 2: Semantic search (fully local, no API cost) ────────────────────────
    chunks = similarity_search(
        query=question,
        top_k=top_k,
        category_filter=category_filter,
    )

    if not chunks:
        return {
            "answer": (
                "Samahani (Sorry), I don't have information on that yet. "
                "Try asking about Masai Mara, Diani Beach, Amboseli, or Nairobi."
            ),
            "sources": [],
            "context_used": 0,
        }

    # ── 3: Build context block from retrieved chunks ──────────────────────────────
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        dest = chunk.get("destination", "Kenya")
        src  = chunk.get("source", "unknown")
        context_parts.append(f"[{i}. {dest} | {src}]\n{chunk['content']}")

    context = "\n\n".join(context_parts)

    # ── 4: Load recent chat history ───────────────────────────────────────────────
    history_messages = []
    if session_id:
        for msg in get_history(session_id, limit=6):
            history_messages.append({"role": msg["role"], "content": msg["content"]})

    # ── 5: Build prompt messages ──────────────────────────────────────────────────
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *history_messages,
        {
            "role": "user",
            "content": (
                f"CONTEXT (use only this to answer):\n"
                f"---\n{context}\n---\n\n"
                f"QUESTION: {question}"
            ),
        },
    ]

    # ── 6: Call Groq (fast + free) ────────────────────────────────────────────────
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.5,
        max_tokens=800,
    )
    answer = response.choices[0].message.content

    # ── 7: Save exchange to history ───────────────────────────────────────────────
    if session_id:
        save_message(session_id, "user", question)
        save_message(session_id, "assistant", answer)

    # ── 8: Return structured result ───────────────────────────────────────────────
    sources = [
        {
            "destination": c.get("destination", "Unknown"),
            "source":      c.get("source", "Unknown"),
            "similarity":  round(c.get("similarity", 0), 3),
        }
        for c in chunks
    ]

    return {
        "answer":       answer,
        "sources":      sources,
        "context_used": len(chunks),
    }


# ── Pydantic models (used by FastAPI) ─────────────────────────────────────────────
class ChatRequest(BaseModel):
    message:         str
    session_id:      Optional[str] = "default"
    category_filter: Optional[str] = None   # e.g. "safari", "beach", "transport"

class ChatResponse(BaseModel):
    answer:       str
    sources:      list
    context_used: int


# ── Quick test ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    questions = [
        "What is the entry fee for Masai Mara?",
        "When is the best time to visit Diani Beach?",
    ]
    for q in questions:
        print(f"\n❓ {q}")
        result = rag_answer(q, session_id="test")
        print(f"🐘 {result['answer'][:200]}...")
        print(f"📚 {[s['destination'] for s in result['sources']]}")