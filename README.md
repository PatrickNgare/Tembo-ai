# 🐘 Tembo AI — Kenya Travel Assistant

> An AI-powered travel assistant built for Kenya, by Kenya.

---

## What is Tembo AI?

Tembo AI is an intelligent travel and tourism assistant that helps users plan trips across Kenya. It uses Retrieval-Augmented Generation (RAG) and LangChain tools to provide accurate, up-to-date travel advice — from safari itineraries to coastal getaways.

---

## Features

- 🗺️ AI-powered Kenya travel planning
- 🌤️ Real-time weather for Kenyan cities
- 💰 Budget estimation (Budget / Mid-range / Luxury)
- 📚 Kenya knowledge base with RAG
- 🧠 Conversation memory
- 🌐 Streamlit web interface

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | OpenAI GPT-4o-mini |
| Orchestration | LangChain |
| Vector DB | ChromaDB |
| Embeddings | OpenAI text-embedding-3-small |
| Web UI | Streamlit |
| Language | Python 3.11+ |

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/tembo-ai.git
cd tembo-ai

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys
cp .env.example .env
# Edit .env with your keys

# 5. Run the app
streamlit run app.py
```

---

## Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=sk-your-key-here
WEATHER_API_KEY=your-openweather-key
GOOGLE_PLACES_KEY=your-google-key
```

---

## Project Structure

```
tembo-ai/
├── app.py                  # Streamlit web app
├── day3_tools.py           # LangChain tools (weather, destinations, budget)
├── day4_knowledge_base.py  # Build the vector knowledge base
├── day4_rag.py             # RAG question answering chain
├── tembo_knowledge_base/   # ChromaDB vector store (auto-generated)
├── requirements.txt
└── .env.example
```

---

## Built With ❤️ in Nairobi



---

*Karibu Kenya! 🇰🇪*
