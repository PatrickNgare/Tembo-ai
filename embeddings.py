"""
embeddings.py
Cloud embeddings using HuggingFace Inference API (FREE).

Same model as before (all-MiniLM-L6-v2), but runs on HuggingFace servers.
This avoids loading the model into memory — works on Render free tier.

Get your free API key at: https://huggingface.co/settings/tokens
"""

import os
import requests
from typing import List
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
API_URL = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{MODEL_ID}"

class HuggingFaceEmbeddings:
    def __init__(self):
        self.api_key = os.getenv("HF_API_KEY") or os.getenv("HUGGINGFACE_API_KEY")
        if not self.api_key:
            print("Warning: HF_API_KEY not set. Get free key at https://huggingface.co/settings/tokens")
        self.headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        self.dimension = 384  # all-MiniLM-L6-v2 output dimension
        print(f"Using HuggingFace Inference API: {MODEL_ID}")

    def _normalize(self, vector: List[float]) -> List[float]:
        """Normalize vector to unit length for cosine similarity."""
        import math
        norm = math.sqrt(sum(x*x for x in vector))
        return [x/norm for x in vector] if norm > 0 else vector

    def embed_text(self, text: str) -> List[float]:
        """Embed a single string."""
        response = requests.post(
            API_URL,
            headers=self.headers,
            json={"inputs": text, "options": {"wait_for_model": True}}
        )
        response.raise_for_status()
        vector = response.json()
        return self._normalize(vector)

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings."""
        response = requests.post(
            API_URL,
            headers=self.headers,
            json={"inputs": texts, "options": {"wait_for_model": True}}
        )
        response.raise_for_status()
        vectors = response.json()
        return [self._normalize(v) for v in vectors]

    # ── LangChain compatibility ─────────────────────────────────────────────────
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embed_batch(texts)

    def embed_query(self, text: str) -> List[float]:
        return self.embed_text(text)


# Singleton — import this everywhere
embedder = HuggingFaceEmbeddings()


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
