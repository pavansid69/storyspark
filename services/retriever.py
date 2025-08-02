import os
import fitz  # PyMuPDF
from typing import List

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter

from config import (
    INDEX_BASE_DIR,  # <- changed from INDEX_DIR
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    EMBEDDING_MODEL_NAME,
    OLLAMA_MODEL_NAME,
    OLLAMA_BASE_URL,
)

embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
llm = Ollama(model=OLLAMA_MODEL_NAME, base_url=OLLAMA_BASE_URL)


def extract_text_from_pdf(pdf_path: str) -> str:
    with fitz.open(pdf_path) as doc:
        return "".join(page.get_text() for page in doc)


def dynamic_chunking(text: str) -> List[str]:
    try:
        splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        return splitter.split_text(text)
    except Exception:
        fallback = CharacterTextSplitter(separator="\n", chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        return fallback.split_text(text)


def index_documents(docs: List, user_id: str, chat_id: str):
    index_dir = os.path.join(INDEX_BASE_DIR, f"user_{user_id}", f"chat_{chat_id}")
    os.makedirs(index_dir, exist_ok=True)
    index_file = os.path.join(index_dir, "index.faiss")

    if os.path.exists(index_file):
        vectorstore = FAISS.load_local(index_dir, embedding_model, allow_dangerous_deserialization=True)
    else:
        vectorstore = FAISS.from_documents(docs, embedding_model)

    vectorstore.add_documents(docs)
    vectorstore.save_local(index_dir)


def query_vectorstore(query: str, user_id: str, chat_id: str) -> str:
    index_dir = os.path.join(INDEX_BASE_DIR, f"user_{user_id}", f"chat_{chat_id}")
    index_file = os.path.join(index_dir, "index.faiss")

    if not os.path.exists(index_file):
        raise ValueError("❌ No indexed data found for this user/chat.")

    vectorstore = FAISS.load_local(index_dir, embedding_model, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)

    if not docs:
        return "😅 Sorry, nothing relevant found."

    context = "\n".join(doc.page_content for doc in docs)
    prompt = (
        f"Answer the following question based on the context below:\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n\nAnswer:"
    )

    return llm.invoke(prompt).strip()