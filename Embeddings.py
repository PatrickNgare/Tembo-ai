"""
embeddings.py
Local embeddings using sentence-transformers.
No API key needed — model runs fully on your machine.

Xenova/Transformers.js is the JavaScript equivalent of this.
In Python we use sentence-transformers, which is the same models under the hood.

Model used: all-MiniLM-L6-v2
  - Fast, lightweight (80MB)
  - 384-dimensional vectors
  - Great for semantic search
  - Runs on CPU, no GPU required
"""

from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

# ── Model is downloaded once, then cached locally in ~/.cache/huggingface ──────
MODEL_NAME = "all-MiniLM-L6-v2"

class LocalEmbeddings:
    def __init__(self, model_name: str = MODEL_NAME):
        print(f"Loading local embedding model: {model_name}")
        print("(First run downloads ~80MB — subsequent runs are instant)")
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()
        print(f"Model ready. Embedding dimension: {self.dimension}")

    def embed_text(self, text: str) -> List[float]:
        """Embed a single string."""
        vector = self.model.encode(text, normalize_embeddings=True)
        return vector.tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings — much faster than one by one."""
        vectors = self.model.encode(texts, normalize_embeddings=True, show_progress_bar=True)
        return vectors.tolist()

    # ── LangChain compatibility ─────────────────────────────────────────────────
    # LangChain expects these two method names on an embeddings object
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embed_batch(texts)

    def embed_query(self, text: str) -> List[float]:
        return self.embed_text(text)


# Singleton — import this everywhere so the model only loads once
embedder = LocalEmbeddings()


# ── Quick test ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_sentences = [
        "Best time to visit Masai Mara",
        "When is the wildebeest migration in Kenya?",   # semantically similar
        "How to cook ugali",                            # completely different
    ]

    vectors = embedder.embed_batch(test_sentences)

    # Cosine similarity (vectors are already normalized, so dot product = cosine sim)
    v0 = np.array(vectors[0])
    v1 = np.array(vectors[1])
    v2 = np.array(vectors[2])

    print(f"\nSimilarity (Mara vs migration): {np.dot(v0, v1):.4f}")  # high
    print(f"Similarity (Mara vs ugali):     {np.dot(v0, v2):.4f}")  # low