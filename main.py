"""
main.py
Tembo AI — FastAPI entry point.

Run:  uvicorn main:app --reload
Docs: http://localhost:8000/docs
"""

import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from rag import ChatRequest, ChatResponse, rag_answer
from vector_store import get_document_count

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="🐘 Tembo AI",
    description="Kenya Travel Assistant — local embeddings + pgvector + Groq (free)",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Health check ─────────────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {
        "status":    "ok",
        "assistant": "Tembo AI 🐘",
        "country":   "Kenya 🇰🇪",
        "stack":     "Groq (Llama 3.3) + pgvector + local embeddings",
    }


# ── Main chat endpoint ────────────────────────────────────────────────────────────
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Send a message → get a Kenya travel answer grounded in the knowledge base.

    - Embeddings: local (sentence-transformers, no quota)
    - Retrieval: PostgreSQL + pgvector
    - Generation: Groq Llama 3.3 70B (free)
    """
    try:
        result = rag_answer(
            question=request.message,
            session_id=request.session_id,
            category_filter=request.category_filter,
        )
        return ChatResponse(**result)
    except Exception as e:
        logger.error(f"Chat endpoint error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# ── DB health check ───────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    """Check database connection and knowledge base size."""
    try:
        count = get_document_count()
        return {
            "status":             "ok",
            "documents_in_kb":    count,
            "embedding_model":    "embed-english-light-v3.0 (Cohere)",
            "llm":                "groq/llama-3.3-70b-versatile",
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"DB error: {str(e)}")


# ── Setup endpoint (populate database) ────────────────────────────────────────────
@app.post("/setup")
def setup_database():
    """One-time setup: populate the database with Kenya travel data."""
    try:
        from massive_kenya_data import populate_massive_database
        result = populate_massive_database()
        return {"status": "ok", "message": "Database populated", "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Setup error: {str(e)}")


# ── Reset endpoint (clear and repopulate database) ────────────────────────────────
@app.post("/reset")
def reset_database():
    """Force clear and repopulate the database with latest Kenya travel data."""
    try:
        from vector_store import clear_knowledge_base
        from massive_kenya_data import populate_massive_database, MASSIVE_KENYA_DATA
        
        # Clear existing data
        clear_knowledge_base()
        logger.info("Database cleared, repopulating...")
        
        # Force repopulate (modify temp to bypass check)
        from vector_store import add_documents_simple
        
        texts = [doc["content"] for doc in MASSIVE_KENYA_DATA]
        metadatas = [
            {
                "source": doc["source"],
                "category": doc["category"],
                "region": doc["region"],
                "destination": doc["destination"],
            }
            for doc in MASSIVE_KENYA_DATA
        ]
        
        # Add in batches
        batch_size = 50
        total_added = 0
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i+batch_size]
            batch_meta = metadatas[i:i+batch_size]
            count = add_documents_simple(batch_texts, batch_meta)
            total_added += count
        
        return {
            "status": "ok", 
            "message": "Database reset complete",
            "documents_added": total_added
        }
    except Exception as e:
        logger.error(f"Reset error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Reset error: {str(e)}")