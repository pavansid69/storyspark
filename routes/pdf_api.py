import os
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from services.retriever import extract_text_from_pdf, dynamic_chunking, index_documents

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(
    user_id: str = Form(...),
    chat_id: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        contents = await file.read()
        temp_path = f"/tmp/{file.filename}"
        with open(temp_path, "wb") as f:
            f.write(contents)

        text = extract_text_from_pdf(temp_path)
        chunks = dynamic_chunking(text)

        # Convert to document format for FAISS
        from langchain_core.documents import Document
        docs = [Document(page_content=chunk) for chunk in chunks]

        index_documents(docs, user_id, chat_id)
        os.remove(temp_path)

        return {"status": "✅ PDF processed & indexed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ PDF processing failed: {e}")