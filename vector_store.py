"""
vector_store.py
PostgreSQL + pgvector vector store for Tembo AI.

Replaces ChromaDB. Uses local embeddings — zero API cost.
"""

import os
import psycopg2
import psycopg2.extras
from typing import List, Optional, Tuple
from dotenv import load_dotenv
from embeddings import embedder

load_dotenv()

# ── Database connection ─────────────────────────────────────────────────────────
DB_CONFIG = {
    "host":     os.getenv("DB_HOST", "localhost"),
    "port":     os.getenv("DB_PORT", "5432"),
    "dbname":   os.getenv("DB_NAME", "tembo_ai"),
    "user":     os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
}


def get_connection():
    """Get a fresh database connection."""
    return psycopg2.connect(**DB_CONFIG)


# ── Write: Add documents to the knowledge base ─────────────────────────────────

def add_documents(
    texts: List[str],
    sources: Optional[List[str]] = None,
    categories: Optional[List[str]] = None,
    regions: Optional[List[str]] = None,
    destinations: Optional[List[str]] = None,
) -> int:
    """
    Embed and store a list of text chunks in PostgreSQL.
    Returns the number of documents inserted.
    """
    if not texts:
        return 0

    print(f"Embedding {len(texts)} documents locally...")
    vectors = embedder.embed_batch(texts)

    rows = []
    for i, (text, vector) in enumerate(zip(texts, vectors)):
        rows.append((
            text,
            vector,
            (sources or [None] * len(texts))[i],
            (categories or [None] * len(texts))[i],
            (regions or [None] * len(texts))[i],
            (destinations or [None] * len(texts))[i],
        ))

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # Register the vector type so psycopg2 can serialize it
            psycopg2.extras.register_default_jsonb(conn)

            insert_sql = """
                INSERT INTO documents (content, embedding, source, category, region, destination)
                VALUES %s
            """
            # Build value tuples with vector cast
            values = [
                cur.mogrify("(%s, %s::vector, %s, %s, %s, %s)", row).decode()
                for row in rows
            ]
            cur.execute(insert_sql.replace("%s", ",".join(values)).replace("VALUES ,", "VALUES "))

            # Simpler approach that always works:
            for row in rows:
                cur.execute(
                    """
                    INSERT INTO documents (content, embedding, source, category, region, destination)
                    VALUES (%s, %s::vector, %s, %s, %s, %s)
                    """,
                    (row[0], str(row[1]), row[2], row[3], row[4], row[5])
                )

        conn.commit()
        print(f"Inserted {len(texts)} documents into PostgreSQL.")
        return len(texts)
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def add_documents_simple(texts: List[str], metadatas: Optional[List[dict]] = None) -> int:
    """
    Simpler version — pass texts and optional metadata dicts.
    Each metadata dict can have: source, category, region, destination
    """
    if metadatas is None:
        metadatas = [{} for _ in texts]

    return add_documents(
        texts=texts,
        sources=[m.get("source") for m in metadatas],
        categories=[m.get("category") for m in metadatas],
        regions=[m.get("region") for m in metadatas],
        destinations=[m.get("destination") for m in metadatas],
    )


# ── Read: Semantic search ───────────────────────────────────────────────────────

def similarity_search(
    query: str,
    top_k: int = 5,
    category_filter: Optional[str] = None,
    region_filter: Optional[str] = None,
) -> List[dict]:
    """
    Find the top_k most semantically similar documents to the query.
    Optionally filter by category or region.

    Returns list of dicts: {content, source, category, region, destination, similarity}
    """
    query_vector = embedder.embed_query(query)
    query_vector_str = str(query_vector)

    # Build filter conditions - params must match order of %s in SQL
    filters = []
    filter_params = []
    if category_filter:
        filters.append("AND category = %s")
        filter_params.append(category_filter)
    if region_filter:
        filters.append("AND region = %s")
        filter_params.append(region_filter)

    # Order: similarity %s, filter %s(s), ORDER BY %s, LIMIT %s
    params = [query_vector_str] + filter_params + [query_vector_str, top_k]

    sql = f"""
        SELECT
            content,
            source,
            category,
            region,
            destination,
            1 - (embedding <=> %s::vector) AS similarity
        FROM documents
        WHERE 1=1
        {" ".join(filters)}
        ORDER BY embedding <=> %s::vector
        LIMIT %s
    """

    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(sql, params)
            results = cur.fetchall()
        return [dict(r) for r in results]
    finally:
        conn.close()


# ── Chat history ────────────────────────────────────────────────────────────────

def save_message(session_id: str, role: str, content: str):
    """Save a chat message to history."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO chat_sessions (session_id, role, content) VALUES (%s, %s, %s)",
                (session_id, role, content)
            )
        conn.commit()
    finally:
        conn.close()


def get_history(session_id: str, limit: int = 10) -> List[dict]:
    """Retrieve recent chat history for a session."""
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                SELECT role, content FROM chat_sessions
                WHERE session_id = %s
                ORDER BY created_at DESC
                LIMIT %s
                """,
                (session_id, limit)
            )
            rows = cur.fetchall()
        # Reverse so oldest message is first
        return [dict(r) for r in reversed(rows)]
    finally:
        conn.close()


# ── Utility ─────────────────────────────────────────────────────────────────────

def get_document_count() -> int:
    """How many documents are in the knowledge base."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM documents")
            return cur.fetchone()[0]
    finally:
        conn.close()


def clear_knowledge_base():
    """Delete all documents. Use with care."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("TRUNCATE TABLE documents RESTART IDENTITY")
        conn.commit()
        print("Knowledge base cleared.")
    finally:
        conn.close()


# ── Quick test ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Add sample documents
    sample_texts = [
        "Masai Mara National Reserve is Kenya's most famous safari destination. Entry fee: $70 USD per adult per day.",
        "The Great Wildebeest Migration happens July to October when 1.5 million wildebeest cross from Tanzania.",
        "Diani Beach is a 17km stretch of white sand south of Mombasa. Best visited December to March.",
        "Nairobi National Park is the only national park in the world inside a capital city. Entry: $43 USD.",
        "Amboseli National Park offers iconic views of Mount Kilimanjaro. Famous for large elephant herds.",
    ]

    sample_meta = [
        {"source": "kws.go.ke", "category": "safari",  "region": "Rift Valley",  "destination": "Masai Mara"},
        {"source": "kws.go.ke", "category": "safari",  "region": "Rift Valley",  "destination": "Masai Mara"},
        {"source": "tourism.go.ke", "category": "beach",  "region": "Coast",     "destination": "Diani Beach"},
        {"source": "kws.go.ke", "category": "safari",  "region": "Nairobi",      "destination": "Nairobi NP"},
        {"source": "kws.go.ke", "category": "safari",  "region": "Rift Valley",  "destination": "Amboseli"},
    ]

    count = add_documents_simple(sample_texts, sample_meta)
    print(f"\nTotal documents in DB: {get_document_count()}")

    print("\n--- Semantic Search Test ---")
    results = similarity_search("game drive and wildlife viewing", top_k=3)
    for r in results:
        print(f"[{r['similarity']:.3f}] {r['destination']}: {r['content'][:80]}...")