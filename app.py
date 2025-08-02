from fastapi import FastAPI
from routes import query_api, pdf_api
import subprocess

app = FastAPI(title="Reel Script Generator API")

# def start_ollama_server():
#     """
#     Start the Ollama server if it's not already running.
#     This avoids errors when generating responses using Ollama-backed LLM.
#     """
#     try:
#         subprocess.Popen(["ollama", "serve"])
#         print("✅ Ollama server started.")
#     except Exception as e:
#         print(f"❌ Failed to start Ollama server: {e}")

# # Run Ollama at startup (can be removed if handled externally)
# start_ollama_server()

# Register all API routers
app.include_router(query_api.router, prefix="/query", tags=["Query-Based Scripts"])
app.include_router(pdf_api.router, prefix="/pdf", tags=["PDF-Based Scripts"])