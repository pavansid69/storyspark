import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
from services.retriever import index_documents


def process_pdf(filename: str, content: bytes, user_id: str, chat_id: str):
    temp_path = f"/tmp/{filename}"
    with open(temp_path, "wb") as f:
        f.write(content)

    loader = PyPDFLoader(temp_path)
    documents = loader.load()

    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            separators=["\n\n", "\n", ".", " ", ""]
        )
        docs = splitter.split_documents(documents)
    except Exception as e:
        print(f"⚠️ Dynamic chunking failed: {e}")
        fallback_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = fallback_splitter.split_documents(documents)

    index_documents(docs, user_id=user_id, chat_id=chat_id)
    os.remove(temp_path)