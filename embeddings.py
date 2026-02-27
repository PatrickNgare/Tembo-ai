"""
embeddings.py
Embeddings using Google Gemini API (FREE).

Gemini provides free embedding API with generous limits.
"""

import os
from typing import List
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)


class GeminiEmbeddings:
    def __init__(self):
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not set. Get free key at https://aistudio.google.com/apikey")
        self.model = "models/embedding-001"
        self.dimension = 768
        print(f"Using Gemini Embeddings: {self.model}")

    def embed_text(self, text: str) -> List[float]:
        """Embed a single string."""
        result = genai.embed_content(
            model=self.model,
            content=text,
            task_type="retrieval_query"
        )
        return result['embedding']

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings."""
        return [self.embed_text(text) for text in texts]

    # ── LangChain compatibility ─────────────────────────────────────────────────
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embed_batch(texts)

    def embed_query(self, text: str) -> List[float]:
        return self.embed_text(text)


# Singleton — import this everywhere
embedder = GeminiEmbeddings()


# ── Quick test ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_sentences = [
        "Best time to visit Masai Mara",
        "When is the wildebeest migration in Kenya?",
        "How to cook ugali",
    ]

    vectors = embedder.embed_batch(test_sentences)

    # Cosine similarity (vectors are normalized, so dot product = cosine sim)
    v0, v1, v2 = vectors[0], vectors[1], vectors[2]
    sim_01 = sum(a*b for a, b in zip(v0, v1))
    sim_02 = sum(a*b for a, b in zip(v0, v2))

    print(f"\nSimilarity (Mara vs migration): {sim_01:.4f}")
    print(f"Similarity (Mara vs ugali):     {sim_02:.4f}")
