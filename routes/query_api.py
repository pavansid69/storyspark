from fastapi import APIRouter
from models.request_models import QueryRequest
from models.response_models import ScriptResponse
from models.request_models import DialogueRequest 
from services.retriever import query_vectorstore
from services.script_builder import build_dialogue_script

router = APIRouter()

@router.post("/generate-from-query", response_model=ScriptResponse)
def generate_from_query(req: QueryRequest):
    context = query_vectorstore(req.query, req.user_id, req.chat_id)
    script = build_dialogue_script(context, req.query, req.characters)
    return ScriptResponse(script=script)

@router.post("/generate-dialogue", response_model=ScriptResponse)
def generate_dialogue_only(req: DialogueRequest):
    """Generate a character-based script from a topic without using vectorstore."""
    context = ""  # No retrieval
    script = build_dialogue_script(context, req.query, req.characters)
    return ScriptResponse(script=script)