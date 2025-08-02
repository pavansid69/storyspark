from services.character_profiles import character_registry
from utils.time_utils import enforce_length_limit

def build_dialogue_script(context: str, query: str, characters: list, dialogue_only=False) -> str:
    """Construct a scripted dialogue between characters using the LLM."""
    speaker_lines = "\n".join([
        f"{char['name']}: {char['description']}" for char in characters
    ])

    prompt = f"""
You are writing a conversational script between characters on the topic:

"{query}"

Characters:
{speaker_lines}

Instructions:
- Keep the dialogue natural and explanatory.
- Avoid scene descriptions or stage directions.
- Make it engaging but informative.
- Keep the conversation around 1 minute in length (~8 to 12 lines).
"""

    if context:
        prompt += f"\nRelevant context:\n{context}\n"

    from services.generator import generate_script_from_prompt
    response = generate_script_from_prompt(prompt).strip()
    return enforce_length_limit(response)