# 🐘 Tembo AI — Kenya Travel Assistant

An AI-powered travel assistant for Kenya, built with FastAPI and a fully free tech stack (no API costs for embeddings!).

---

## 🚀 Quick Start

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

The API will be live at `http://localhost:8000`  
Interactive docs at `http://localhost:8000/docs`

---

## 📁 Project Structure

```
tembo-ai/
├── main.py                 # FastAPI app entry point
├── rag.py                  # RAG pipeline (retrieval + generation)
├── embeddings.py           # Local embeddings (sentence-transformers)
├── vector_store.py         # PostgreSQL + pgvector vector store
├── setup_vector.py         # SQL schema for pgvector setup
├── scrape_kenya_data.py    # Web scraper for Kenya travel data
├── massive_kenya_data.py   # Curated Kenya knowledge base (200+ docs)
├── requirements.txt
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
# Groq API (free tier available)
GROQ_API_KEY=gsk_your-groq-key-here

# PostgreSQL Database
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
  -d '{"message": "Plan a 5-day trip to Masai Mara", "session_id": "user123"}'
```

### Example Response

```json
{
  "answer": "Karibu! Here is your 5-day Masai Mara itinerary...",
  "sources": ["kws.go.ke", "magicalkenya.com"],
  "context_used": 5
}
```

---

## 🛠️ Tech Stack (100% Free for Development)

- **FastAPI** — High-performance API framework
- **PostgreSQL + pgvector** — Vector database with HNSW indexing
- **sentence-transformers** — Local embeddings (all-MiniLM-L6-v2, 384-dim)
- **Groq API** — Free LLM inference (Llama 3.3 70B Versatile)
- **BeautifulSoup** — Web scraping for knowledge base

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

## 📦 Key Dependencies

```
fastapi
uvicorn
groq
psycopg2-binary
sentence-transformers
beautifulsoup4
requests
python-dotenv
pydantic
```

---

## 🌍 Knowledge Base

The knowledge base includes 200+ documents covering:
- **National Parks**: Masai Mara, Amboseli, Tsavo East/West, Lake Nakuru, etc.
- **Beaches**: Diani, Watamu, Malindi, Lamu
- **Cities**: Nairobi, Mombasa, Kisumu
- **Practical Info**: Entry fees, transport, accommodation, safety tips

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

MIT

---

*Built with ❤️ in Nairobi, Kenya 🇰🇪*

