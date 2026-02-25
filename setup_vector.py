-- ============================================================
-- setup_pgvector.sql
-- Run this once to set up your PostgreSQL database for Tembo AI
-- ============================================================

-- 1. Enable the pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Create the documents table
--    dim = 384 to match all-MiniLM-L6-v2 embeddings
CREATE TABLE IF NOT EXISTS documents (
    id          SERIAL PRIMARY KEY,
    content     TEXT        NOT NULL,           -- the raw text chunk
    embedding   VECTOR(384) NOT NULL,           -- local model produces 384-dim vectors
    source      TEXT,                           -- e.g. 'kws.go.ke', 'manual'
    category    TEXT,                           -- 'safari', 'beach', 'transport', etc.
    region      TEXT,                           -- 'Coast', 'Rift Valley', 'Nairobi', etc.
    destination TEXT,                           -- e.g. 'Masai Mara', 'Diani Beach'
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Create an HNSW index for fast approximate nearest-neighbour search
--    HNSW is faster than IVFFlat for most use cases
--    operator class: vector_cosine_ops (matches normalized embeddings)
CREATE INDEX IF NOT EXISTS documents_embedding_idx
    ON documents
    USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);

-- 4. Create chat history table (for conversation memory)
CREATE TABLE IF NOT EXISTS chat_sessions (
    id          SERIAL PRIMARY KEY,
    session_id  TEXT        NOT NULL,
    role        TEXT        NOT NULL,           -- 'user' or 'assistant'
    content     TEXT        NOT NULL,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS chat_sessions_session_idx
    ON chat_sessions (session_id, created_at);

-- ============================================================
-- Verify setup
-- ============================================================
SELECT 'pgvector extension active' AS status WHERE EXISTS (
    SELECT 1 FROM pg_extension WHERE extname = 'vector'
);
SELECT 'documents table ready' AS status WHERE EXISTS (
    SELECT 1 FROM information_schema.tables WHERE table_name = 'documents'
);