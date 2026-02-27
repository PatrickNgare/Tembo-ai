# 🐘 Tembo AI — Kenya Travel Assistant

An AI-powered travel assistant for Kenya with a beautiful React frontend and a fully free tech stack.

**🚀 Live Demo:** [https://tembo-ai-frontend.onrender.com](https://tembo-ai-frontend.onrender.com)

![Tembo AI](https://img.shields.io/badge/Kenya-Travel%20Assistant-success?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48dGV4dCB5PSIuOWVtIiBmb250LXNpemU9IjkwIj7wn5GNPC90ZXh0Pjwvc3ZnPg==)

---

## ✨ Features

- 🦁 **Smart RAG Pipeline** — Retrieval-augmented generation for accurate Kenya travel info
- 💬 **Conversational AI** — Personalized responses with Swahili flair
- 🎨 **Beautiful UI** — Modern React + Tailwind CSS frontend with animations
- ⚡ **Real-time Typing Effect** — Character-by-character response display
- 🏷️ **Category Filters** — Filter by Safari, Beaches, Culture, Transport
- 📊 **Source Attribution** — See which documents informed each answer
- 🆓 **100% Free Stack** — Cohere embeddings + Groq LLM + Supabase

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | React + Tailwind CSS |
| **Backend** | FastAPI (Python) |
| **Embeddings** | Cohere `embed-english-light-v3.0` (free tier) |
| **LLM** | Groq `llama-3.3-70b-versatile` (free tier) |
| **Vector DB** | PostgreSQL + pgvector (Supabase) |
| **Hosting** | Render (free tier) |

---

## 🚀 Quick Start

### Backend

```bash
# Clone the repo
git clone https://github.com/your-username/tembo-ai.git
cd tembo-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL with pgvector
psql -U postgres -f setup_vector.py  # Run SQL commands to create tables

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys

# Populate the knowledge base
python massive_kenya_data.py  # Or: python scrape_kenya_data.py

# Run the server
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

- **Backend API**: `http://localhost:8000`
- **Frontend UI**: `http://localhost:5173`
- **API Docs**: `http://localhost:8000/docs`

---

## 📁 Project Structure

```
tembo-ai/
├── main.py                 # FastAPI app entry point
├── rag.py                  # RAG pipeline (retrieval + generation)
├── embeddings.py           # Cohere embeddings API
├── vector_store.py         # PostgreSQL + pgvector vector store
├── setup_vector.py         # SQL schema for pgvector setup
├── scrape_kenya_data.py    # Web scraper for Kenya travel data
├── massive_kenya_data.py   # Curated Kenya knowledge base (188 docs)
├── sample_requests.json    # Example API requests
├── requirements.txt
├── render.yaml             # Render deployment config
├── frontend/               # React + Tailwind CSS frontend
│   ├── src/
│   │   ├── App.jsx         # Main chat component
│   │   └── index.css       # Tailwind + custom animations
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
# Groq API (free tier - https://console.groq.com)
GROQ_API_KEY=gsk_your-groq-key-here

# Cohere API (free tier - https://dashboard.cohere.com/api-keys)
COHERE_API_KEY=your-cohere-key-here

# PostgreSQL Database (Supabase)
DATABASE_URL=postgresql://postgres.[project-ref]:[password]@aws-0-us-east-1.pooler.supabase.com:6543/postgres

# Or for local development:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=tembo_ai
DB_USER=postgres
DB_PASSWORD=your-password
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check + stack info |
| `POST` | `/chat` | Send a message to Tembo |
| `GET` | `/health` | Check DB connection & KB size |

### Example Request

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Plan a 5-day trip to Masai Mara",
    "session_id": "user123",
    "category_filter": "safari"
  }'
```

### Example Response

```json
{
  "answer": "Jambo! 🦁 The Mara will absolutely blow your mind! Here's your 5-day adventure...",
  "sources": [
    {"destination": "Masai Mara", "source": "kws.go.ke", "similarity": 0.89},
    {"destination": "Masai Mara", "source": "magicalkenya.com", "similarity": 0.85}
  ],
  "context_used": 5
}
```

---

## 🛠️ Tech Stack

### Backend (100% Free for Development)
- **FastAPI** — High-performance async API framework
- **PostgreSQL + pgvector** — Vector database with HNSW indexing
- **sentence-transformers** — Local embeddings (all-MiniLM-L6-v2, 384-dim)
- **Groq API** — Free LLM inference (Llama 3.3 70B Versatile)
- **BeautifulSoup** — Web scraping for knowledge base

### Frontend
- **React 18** — UI framework with hooks
- **Vite** — Lightning-fast build tool
- **Tailwind CSS v4** — Utility-first styling
- **Custom Animations** — Typing effect, slide-up, floating elements

---

## 🗄️ Database Setup

1. Install PostgreSQL and pgvector extension
2. Create the database:
   ```sql
   CREATE DATABASE tembo_ai;
   ```
3. Run the setup SQL from `setup_vector.py`:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   
   CREATE TABLE documents (
       id SERIAL PRIMARY KEY,
       content TEXT NOT NULL,
       embedding VECTOR(384) NOT NULL,
       source TEXT,
       category TEXT,
       region TEXT,
       destination TEXT,
       created_at TIMESTAMPTZ DEFAULT NOW()
   );
   
   CREATE TABLE chat_sessions (
       id SERIAL PRIMARY KEY,
       session_id TEXT NOT NULL,
       role TEXT NOT NULL,
       content TEXT NOT NULL,
       created_at TIMESTAMPTZ DEFAULT NOW()
   );
   ```

---

## 🌍 Knowledge Base

The knowledge base includes **376+ documents** covering:

| Category | Topics |
|----------|--------|
| 🦁 Safari | Masai Mara, Amboseli, Tsavo, Lake Nakuru, Samburu |
| 🏖️ Beaches | Diani, Watamu, Malindi, Lamu, Nyali |
| 🏙️ Cities | Nairobi, Mombasa, Kisumu, Nakuru |
| 🚗 Transport | SGR trains, flights, matatus, road trips |
| 💰 Practical | Entry fees, visas, safety, best times to visit |

---

## 🎨 Frontend Features

- **Animated Background** — Gradient orbs with glassmorphism
- **Typing Effect** — Character-by-character response reveal
- **Category Filters** — Quick filter by topic (Safari 🦁, Beaches 🏖️, etc.)
- **Source Tags** — See similarity scores for retrieved documents
- **Suggestion Chips** — Quick-start conversation prompts
- **Dark Theme** — Kenya-inspired emerald and amber colors
- **Responsive Design** — Works on mobile and desktop

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

MIT

---

*Built with ❤️ for Kenya 🇰🇪 — Karibu sana!*

