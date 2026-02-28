# 🏗️ Tembo AI — Technical Architecture

A production-ready RAG (Retrieval-Augmented Generation) application built entirely on free-tier services.

---

## 📐 System Architecture

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│                 │      │                 │      │                 │
│  React Frontend │─────▶│  FastAPI        │─────▶│  Groq LLM       │
│  (Vite + TW)    │      │  Backend        │      │  Llama 3.3 70B  │
│                 │      │                 │      │                 │
└─────────────────┘      └────────┬────────┘      └─────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
          ┌─────────────────┐      ┌─────────────────┐
          │  Cohere         │      │  Supabase       │
          │  Embeddings     │      │  PostgreSQL     │
          │  (1024-dim)     │      │  + pgvector     │
          └─────────────────┘      └─────────────────┘
```

---

## 📊 RAG Pipeline

### Request Flow

```
User Query
    │
    ▼
┌───────────────────────────────────────────────────────────────┐
│ 1. EMBEDDING                                                  │
│    • Model: Cohere embed-english-light-v3.0                   │
│    • Dimensions: 1024                                         │
│    • Latency: ~200ms                                          │
└───────────────────────────────────────────────────────────────┘
    │
    ▼
┌───────────────────────────────────────────────────────────────┐
│ 2. RETRIEVAL                                                  │
│    • Vector search: pgvector cosine similarity                │
│    • Top-k: 5 documents                                       │
│    • Similarity threshold: 0.3                                │
│    • Optional: category/region metadata filtering             │
│    • Latency: ~50ms                                           │
└───────────────────────────────────────────────────────────────┘
    │
    ▼
┌───────────────────────────────────────────────────────────────┐
│ 3. CONTEXT ASSEMBLY                                           │
│    • System prompt (Tembo personality + rules)                │
│    • Retrieved documents with metadata                        │
│    • Chat history (session-based)                             │
│    • User query                                               │
└───────────────────────────────────────────────────────────────┘
    │
    ▼
┌───────────────────────────────────────────────────────────────┐
│ 4. GENERATION                                                 │
│    • Model: Llama 3.3 70B Versatile (via Groq)                │
│    • Context window: 8192 tokens                              │
│    • Temperature: 0.7                                         │
│    • Latency: ~1-2s                                           │
└───────────────────────────────────────────────────────────────┘
    │
    ▼
Response with Sources
```

---

## 🗄️ Database Schema

### PostgreSQL + pgvector

```sql
-- Vector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Knowledge base documents
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    embedding VECTOR(1024) NOT NULL,  -- Cohere embeddings
    source TEXT,                       -- e.g., "kws.go.ke"
    category TEXT,                     -- safari, beach, culture, transport
    region TEXT,                       -- Coast, Rift Valley, Nairobi, etc.
    destination TEXT,                  -- Masai Mara, Diani Beach, etc.
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- HNSW index for fast similarity search
CREATE INDEX ON documents 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- Chat history for session continuity
CREATE TABLE chat_sessions (
    id SERIAL PRIMARY KEY,
    session_id TEXT NOT NULL,
    role TEXT NOT NULL,               -- 'user' or 'assistant'
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_session ON chat_sessions(session_id);
```

---

## 🔧 Component Details

### Frontend (React + Vite)

| Component | Technology | Purpose |
|-----------|------------|---------|
| Framework | React 18 | UI components with hooks |
| Build Tool | Vite 5 | Fast HMR and builds |
| Styling | Tailwind CSS v4 | Utility-first CSS |
| Animations | Custom CSS | Typing effect, slide-up, floating orbs |
| State | useState/useEffect | Local component state |
| HTTP | fetch API | Backend communication |

**Key Features:**
- Character-by-character typing animation
- Category filter buttons (Safari, Beaches, Culture, Transport)
- Source attribution with similarity scores
- Suggestion chips for quick queries
- Responsive glassmorphism design

### Backend (FastAPI)

| Component | Technology | Purpose |
|-----------|------------|---------|
| Framework | FastAPI | Async API with auto-docs |
| Validation | Pydantic v2 | Request/response models |
| DB Driver | psycopg2 | PostgreSQL connection |
| Config | python-dotenv | Environment variables |
| CORS | FastAPI middleware | Cross-origin requests |

**Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check + stack info |
| `POST` | `/chat` | Main RAG endpoint |
| `GET` | `/health` | DB connection + document count |
| `POST` | `/setup` | Populate knowledge base |
| `POST` | `/reset` | Clear and repopulate KB |

### Embedding Layer (Cohere)

```python
# embeddings.py
model = "embed-english-light-v3.0"
dimensions = 1024
input_type = "search_document"  # for KB ingestion
input_type = "search_query"     # for user queries
```

**Why Cohere?**
- Free tier: 1000 embeddings/minute
- High-quality multilingual embeddings
- `search_document` vs `search_query` optimization

### Vector Store (pgvector)

```python
# Similarity search query
SELECT content, source, category, region, destination,
       1 - (embedding <=> %s) AS similarity
FROM documents
WHERE category = %s  -- optional filter
ORDER BY embedding <=> %s
LIMIT 5;
```

**Index Configuration:**
- Algorithm: HNSW (Hierarchical Navigable Small World)
- `m = 16` (connections per node)
- `ef_construction = 64` (build-time search depth)
- Distance: Cosine similarity

### LLM Layer (Groq)

```python
# rag.py
model = "llama-3.3-70b-versatile"
temperature = 0.7
max_tokens = 1024
```

**Why Groq?**
- Free tier: 30 requests/min, 6000/day
- Fastest inference (~200 tokens/sec)
- Llama 3.3 70B quality

---

## ⚡ Performance Metrics

| Stage | Latency | Notes |
|-------|---------|-------|
| Cohere Embedding | ~200ms | Single query embedding |
| pgvector Search | ~50ms | HNSW index, top-5 |
| Groq Generation | ~1-2s | Depends on response length |
| **Total E2E** | **~1.5-2.5s** | Full RAG pipeline |

---

## 💰 Cost Analysis (Free Tier)

| Service | Free Tier Limits | Our Usage |
|---------|------------------|-----------|
| **Cohere** | 1000 embeddings/min | ~5-10/min |
| **Groq** | 30 req/min, 6000/day | ~10-20/day |
| **Supabase** | 500MB DB, 2GB bandwidth | ~50MB |
| **Render** | 750 hours/month | Always-on |

**Monthly Cost: $0** 🎉

---

## 📁 File Structure

```
tembo-ai/
├── main.py                 # FastAPI entry point, routes
├── rag.py                  # RAG pipeline, Groq integration
├── embeddings.py           # Cohere embedding wrapper
├── vector_store.py         # pgvector operations
├── massive_kenya_data.py   # Knowledge base (233 documents)
├── setup_vector.py         # Database schema setup
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Main chat component
│   │   ├── main.jsx        # React entry point
│   │   └── index.css       # Tailwind + animations
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
└── ARCHITECTURE.md         # This file
```

---

## 🔐 Environment Variables

```env
# LLM (Groq)
GROQ_API_KEY=gsk_...

# Embeddings (Cohere)
COHERE_API_KEY=...

# Database (Supabase)
DATABASE_URL=postgresql://postgres.[ref]:[pass]@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```

---

## 🚀 Deployment

### Render Configuration (render.yaml)

```yaml
services:
  # Backend API
  - type: web
    name: backend-tembo-ai
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: GROQ_API_KEY
        sync: false
      - key: COHERE_API_KEY
        sync: false
      - key: DATABASE_URL
        sync: false

  # Frontend
  - type: web
    name: tembo-ai-frontend
    runtime: static
    buildCommand: cd frontend && npm install && npm run build
    staticPublishPath: frontend/dist
```

---

## 🔄 Data Flow Example

**User asks:** "What hotels are at Tiwi Beach?"

```
1. Frontend sends POST /chat
   {
     "message": "What hotels are at Tiwi Beach?",
     "session_id": "user123"
   }

2. Backend embeds query via Cohere
   → [0.023, -0.156, 0.089, ...] (1024 dims)

3. pgvector finds similar documents
   → "Tiwi Beach accommodation: Sand Island..."
   → "Tiwi Beach is located 17 km south..."
   → "Getting to Tiwi Beach: Cross Likoni..."

4. Context assembled for Groq
   SYSTEM: You are Tembo 🐘, a Kenya travel guide...
   CONTEXT: [retrieved documents]
   USER: What hotels are at Tiwi Beach?

5. Groq generates response
   → "Jambo! 🐘 Here are stays at Tiwi Beach:
      • Sand Island Beach Cottages ($40-80/night)
      • Tiwi Sea Castles ($50-100/night)..."

6. Response returned with sources
   {
     "answer": "Jambo! 🐘 Here are stays...",
     "sources": [
       {"destination": "Tiwi Beach", "similarity": 0.64}
     ],
     "context_used": 5
   }
```

---

## 📚 Knowledge Base Coverage

| Category | Documents | Topics |
|----------|-----------|--------|
| 🦁 Safari | 80+ | Masai Mara, Amboseli, Tsavo, Samburu, Lake Nakuru |
| 🏖️ Beaches | 40+ | Diani, Tiwi, Watamu, Malindi, Lamu, Mombasa |
| 🏙️ Cities | 25+ | Nairobi attractions, Mombasa Old Town |
| 🚗 Transport | 30+ | SGR trains, flights, matatus, visas |
| 🍽️ Culture | 30+ | Food, tribes, Maasai, Swahili customs |
| 💰 Practical | 25+ | Costs, safety, best times, packing |

**Total: 233 curated documents**

---

## 🛠️ Future Improvements

- [ ] Streaming responses (SSE)
- [ ] Multi-turn conversation memory
- [ ] Image support for destinations
- [ ] Voice input/output
- [ ] Itinerary builder tool
- [ ] Booking integrations

---

*Built with ❤️ for Kenya 🇰🇪*
