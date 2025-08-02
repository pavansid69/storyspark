import os
from dotenv import load_dotenv

load_dotenv()  

# Base directory for storing vector indexes
INDEX_BASE_DIR = os.getenv("INDEX_BASE_DIR", "vectorstore")

# PDF chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

# Embeddings & LLM
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL", "mistral")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")