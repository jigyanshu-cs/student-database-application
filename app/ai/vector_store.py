from pathlib import Path
import chromadb
from app.config import CHROMA_PATH
def get_collection():
    Path(CHROMA_PATH).mkdir(parents=True,exist_ok=True)
    return chromadb.PersistentClient(path=CHROMA_PATH).get_or_create_collection('project_knowledge')
def seed_project_knowledge():
    c=get_collection(); docs=['FastAPI exposes REST APIs and Swagger documentation.','LangGraph orchestrates Gemini and student database tools.','ChromaDB stores project knowledge for semantic retrieval.','PostgreSQL stores persistent student records.','JWT authentication protects student and chatbot endpoints.']; c.upsert(ids=[f'doc-{i}' for i in range(len(docs))],documents=docs)
def search_knowledge(q,n=3): return get_collection().query(query_texts=[q],n_results=n).get('documents',[[]])[0]
