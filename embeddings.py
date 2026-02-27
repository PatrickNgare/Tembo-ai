"""
embeddings.py
Embeddings using Jina AI (FREE - 1M tokens/month).

Reliable free embedding API, no API key required for basic usage.
"""

import os
import requests
from typing import List
from dotenv import load_dotenv

load_dotenv()

# Jina AI free embeddings - no API key needed!
JINA_API_URL = "https://api.jina.ai/v1/embeddings"


class JinaEmbeddings:
    def __init__(self):
        self.model = "jina-embeddings-v2-base-en"
        self.dimension = 768
        self.headers = {
            "Content-Type": "application/json",
        }
        # Optional: Add API key for higher limits
        jina_key = os.getenv("JINA_API_KEY")
        if jina_key:
            self.headers["Authorization"] = f"Bearer {jina_key}"
        print(f"Using Jina Embeddings: {self.model}")

    def embed_text(self, text: str) -> List[float]:
        """Embed a single string."""
        response = requests.post(
            JINA_API_URL,
            headers=self.headers,
            json={
                "model": self.model,
                "input": [text]
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings."""
        # Batch for efficiency
        response = requests.post(
            JINA_API_URL,
            headers=self.headers,
            json={
                "model": self.model,
                "input": texts
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()["data"]
        return [item["embedding"] for item in data]

    # ── LangChain compatibility ─────────────────────────────────────────────────
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embed_batch(texts)

    def embed_query(self, text: str) -> List[float]:
        return self.embed_text(text)


# Singleton — import this everywhere
embedder = JinaEmbeddings()


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
