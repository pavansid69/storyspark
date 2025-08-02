def enforce_length_limit(script: str, max_words: int = 70) -> str:
    words = script.split()
    if len(words) > max_words:
        return " ".join(words[:max_words]) + "..."
    return script