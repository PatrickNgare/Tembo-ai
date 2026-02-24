# 🐘 Tembo AI — Kenya Travel Assistant

An AI-powered travel assistant for Kenya, built with FastAPI and LangChain.

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

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys

# Run the server
uvicorn main:app --reload
```

The API will be live at `http://localhost:8000`  
Interactive docs at `http://localhost:8000/docs`

---

## 📁 Project Structure

```
tembo-ai/
├── main.py              # FastAPI app entry point
├── routes/
│   ├── chat.py          # Chat endpoints
│   └── itinerary.py     # Itinerary generation
├── tools/
│   ├── weather.py       # Weather API tool
│   ├── destinations.py  # Kenya destinations lookup
│   └── budget.py        # Budget calculator
├── knowledge/
│   └── tembo_kb/        # ChromaDB vector store
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-your-key-here
WEATHER_API_KEY=your-openweather-key
GOOGLE_PLACES_KEY=your-google-key
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/chat` | Send a message to Tembo |
| `POST` | `/itinerary` | Generate a travel itinerary |
| `GET` | `/destinations` | List Kenya destinations |

### Example Request

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Plan a 5-day trip to Masai Mara"}'
```

### Example Response

```json
{
  "response": "Karibu! Here is your 5-day Masai Mara itinerary...",
  "sources": ["masai_mara_guide", "kws_park_fees"]
}
```

---

## 🛠️ Tech Stack

- **FastAPI** — API framework
- **LangChain** — AI orchestration & RAG pipeline
- **OpenAI GPT-4o-mini** — Language model
- **ChromaDB** — Vector database for Kenya knowledge base
- **OpenWeatherMap API** — Live weather data

---

## 📦 Requirements

```
fastapi
uvicorn
openai
langchain
langchain-openai
langchain-community
chromadb
tiktoken
requests
python-dotenv
pydantic
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

MIT

---

*Built with ❤️ in Nairobi, Kenya 🇰🇪*
