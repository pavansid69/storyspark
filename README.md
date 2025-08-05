# 🎬 StorySpark – AI-Powered Script Generator for Educational Reels

**StorySpark** is an AI-first backend service that transforms user queries or uploaded PDFs into short, engaging scripts using predefined pop culture characters like *Family Guy* or *Rick and Morty*. It's designed for fast, character-driven script generation — ideal for educational reels and bite-sized learning.

---

## 🚀 Why StorySpark?

Many learners today struggle with long-form content and short attention spans. StorySpark solves this by:
- Turning information into **fun, memorable conversations**
- Letting users choose **character-driven delivery styles**
- Supporting both **manual queries** and **document uploads**

This is part of a larger personal project aimed at making learning more accessible and engaging for everyone — especially visual and auditory learners.

---

## 🛠 Features

- ✅ Query-based script generation (multi-character dialogues)
- ✅ PDF upload and RAG-based summarization
- ✅ Ollama + LangChain + Sentence Transformers
- ✅ Dockerized for easy local testing

---

## 🧱 Tech Stack

- **FastAPI** – REST API backend
- **LangChain** – Orchestrating RAG pipelines
- **Ollama** – Local LLM server (e.g., Mistral)
- **HuggingFace Embeddings** – for vector similarity
- **Docker Compose** – Multi-container setup
- **FAISS** – for storing and querying vectorized chunks

---

## 📦 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/pavansid69/storyspark.git
cd storyspark
```

### 2. Build & Run the containers

```bash
docker-compose up --build
```

This starts:
- ollama server (port 11434)
- rag-llm-api FastAPI backend (port 8000)

---

## 📡 API Endpoints to Test

### 🔍 Query-based Dialogue Generation

```bash
curl -X POST http://localhost:8000/query/generate-dialogue \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is the future of AI?",
    "characters": [
      { "name": "Peter", "description": "A laid-back, humorous guy" },
      { "name": "Stewie", "description": "A sarcastic and smart baby" }
    ]
  }'
```

### 📄 Upload PDF and Create Vector Store

```bash
curl -X POST -F "file=@/full/path/to/your-file.pdf" \
  "http://localhost:8000/pdf/upload-pdf?user_id=user1&chat_id=chat1"
```

*Replace `@/full/path/to/your-file.pdf` with the absolute path of your PDF.*

### 💬 Generate Dialogue from Uploaded PDF

```bash
curl -X POST http://localhost:8000/pdf/generate-dialogue \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user1",
    "chat_id": "chat1",
    "query": "Summarize this document",
    "characters": [
      { "name": "Peter", "description": "A laid-back, humorous guy" },
      { "name": "Stewie", "description": "A sarcastic and smart baby" }
    ]
  }'
```

---

## 📌 Project Structure

```
storyspark/
├── services/
│   ├── generator.py       # LLM query service
│   ├── retriever.py       # PDF vector store + similarity retriever
│   └── pdf_processor.py   # Chunking and embedding
├── routes/
│   ├── query_api.py       # /query endpoints
│   └── pdf_api.py         # /pdf endpoints
├── app.py                 # FastAPI entry point
├── Dockerfile             # Backend Docker config
├── docker-compose.yml     # Multi-service container setup
└── README.md              # You are here
```

---

## 🧠 Future Roadmap

- UI for uploading PDFs and picking characters
- TTS voiceover generation (ElevenLabs, Coqui, etc.)
- Reels video rendering
- Session-based document/chat history
- Public hosting (Render / EC2 / Hugging Face Spaces)

---

## 🙌 Contributions Welcome

This is still in progress. If you're a dev, designer, or AI enthusiast with ideas — feel free to:
- Suggest new characters
- Help with audio / video generation
- Recommend UX improvements

---

## 📣 Credits

- LangChain
- Ollama
- FAISS
- HuggingFace Transformers
- FastAPI

---

## 👋 Author

**Pavan Sidhartha Reddymasu**
- 📍 [LinkedIn](https://www.linkedin.com/in/pavan-sidhartha-reddymasu-257a71184/)
- 💻 [GitHub](https://github.com/pavansid69)
