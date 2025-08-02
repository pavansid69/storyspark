from pydantic import BaseModel
from typing import List, Dict

class QueryRequest(BaseModel):
    query: str
    user_id: str
    chat_id: str
    characters: List[Dict[str, str]]  # Each dict should have 'name' and 'description'

class PDFScriptRequest(BaseModel):
    pdf_path: str
    query: str
    characters: List[Dict[str, str]]

class DialogueRequest(BaseModel):
    query: str  # Changed from 'topic' for consistency
    characters: List[Dict[str, str]]