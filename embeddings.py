"""
embeddings.py
Embeddings using Google Gemini API (FREE) via REST.

Uses direct REST API to avoid deprecated package issues.
"""

import os
import requests
from typing import List
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class GeminiEmbeddings:
    def __init__(self):
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not set. Get free key at https://aistudio.google.com/apikey")
        self.model = "text-embedding-004"
        self.dimension = 768
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:embedContent"
        print(f"Using Gemini Embeddings: {self.model}")

    def embed_text(self, text: str) -> List[float]:
        """Embed a single string."""
        response = requests.post(
            f"{self.api_url}?key={GOOGLE_API_KEY}",
            json={
                "model": f"models/{self.model}",
                "content": {"parts": [{"text": text}]}
            },
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        response.raise_for_status()
        return response.json()["embedding"]["values"]

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
