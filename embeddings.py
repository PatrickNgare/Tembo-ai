"""
embeddings.py
Local embeddings using sentence-transformers.

The all-MiniLM-L6-v2 model is only ~90MB and runs fine on Render free tier.
"""

import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "all-MiniLM-L6-v2"

class LocalEmbeddings:
    def __init__(self):
        from sentence_transformers import SentenceTransformer
        print(f"Loading embedding model: {MODEL_NAME}...")
        self.model = SentenceTransformer(MODEL_NAME)
        self.dimension = 384  # all-MiniLM-L6-v2 output dimension
        print(f"Model loaded successfully!")

    def embed_text(self, text: str) -> List[float]:
        """Embed a single string."""
        vector = self.model.encode(text, normalize_embeddings=True)
        return vector.tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings."""
        vectors = self.model.encode(texts, normalize_embeddings=True)
        return vectors.tolist()

    # ── LangChain compatibility ─────────────────────────────────────────────────
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embed_batch(texts)

    def embed_query(self, text: str) -> List[float]:
        return self.embed_text(text)


# Singleton — import this everywhere
embedder = LocalEmbeddings()


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
