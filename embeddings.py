"""
embeddings.py
Embeddings using Cohere API (FREE tier - 100 calls/min).

Get free API key at: https://dashboard.cohere.com/api-keys
"""

import os
import requests
from typing import List
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")


class CohereEmbeddings:
    def __init__(self):
        if not COHERE_API_KEY:
            raise ValueError("COHERE_API_KEY not set. Get free key at https://dashboard.cohere.com/api-keys")
        self.model = "embed-english-light-v3.0"  # Free tier model
        self.dimension = 384
        self.api_url = "https://api.cohere.ai/v1/embed"
        self.headers = {
            "Authorization": f"Bearer {COHERE_API_KEY}",
            "Content-Type": "application/json",
        }
        print(f"Using Cohere Embeddings: {self.model}")

    def embed_text(self, text: str) -> List[float]:
        """Embed a single string."""
        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={
                "model": self.model,
                "texts": [text],
                "input_type": "search_query",
                "truncate": "END"
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()["embeddings"][0]

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings."""
        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={
                "model": self.model,
                "texts": texts,
                "input_type": "search_document",
                "truncate": "END"
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json()["embeddings"]

    # ── LangChain compatibility ─────────────────────────────────────────────────
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embed_batch(texts)

    def embed_query(self, text: str) -> List[float]:
        return self.embed_text(text)


# Singleton — import this everywhere
embedder = CohereEmbeddings()


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
