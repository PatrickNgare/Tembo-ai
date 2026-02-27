"""
embeddings.py
Local embeddings using FastEmbed (ONNX-based, no PyTorch needed).

Much lighter than sentence-transformers, works well on Render free tier.
"""

import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "BAAI/bge-small-en-v1.5"  # Small, fast, good quality

class LocalEmbeddings:
    def __init__(self):
        from fastembed import TextEmbedding
        print(f"Loading embedding model: {MODEL_NAME}...")
        self.model = TextEmbedding(model_name=MODEL_NAME)
        self.dimension = 384  # bge-small-en output dimension
        print(f"Model loaded successfully!")

    def embed_text(self, text: str) -> List[float]:
        """Embed a single string."""
        vectors = list(self.model.embed([text]))
        return vectors[0].tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings."""
        vectors = list(self.model.embed(texts))
        return [v.tolist() for v in vectors]

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
