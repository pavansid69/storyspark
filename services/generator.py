import requests
from config import OLLAMA_BASE_URL, OLLAMA_MODEL_NAME


def generate_script_from_prompt(prompt: str) -> str:
    """Generate a response from Ollama using the configured model and base URL."""
    payload = {
        "model": OLLAMA_MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, timeout=120)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"❌ Ollama request failed: {e}")

    return response.json().get("response", "").strip()