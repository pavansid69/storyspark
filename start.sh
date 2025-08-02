#!/bin/bash

# Start Ollama in the background
ollama serve &

# Wait until Ollama server is up
echo "🟡 Waiting for Ollama to be ready..."
until curl -s "$OLLAMA_BASE_URL/api/tags" > /dev/null; do
    sleep 1
done

# Pull the model if not already available
ollama list | grep "$OLLAMA_MODEL" || ollama pull "$OLLAMA_MODEL"

echo "✅ Ollama is ready. Starting FastAPI app..."
exec uvicorn app:app --host 0.0.0.0 --port 8000