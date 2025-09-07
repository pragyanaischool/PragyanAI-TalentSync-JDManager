import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Backend
    frontend_origins: list[str] = os.getenv("FRONTEND_ORIGINS", "*").split(",")

    # MongoDB
    mongo_uri: str = os.getenv("MONGO_URI")
    mongo_db_name: str = os.getenv("MONGO_DB_NAME", "job_descriptions_db")
    mongo_collection_name: str = os.getenv("MONGO_COLLECTION_NAME", "jd_collection")
    mongo_vector_collection_name: str = os.getenv("MONGO_VECTOR_COLLECTION_NAME", "jd_vectors")

    # LLM Provider
    llm_provider: str = os.getenv("LLM_PROVIDER", "groq")

    # API Keys
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")

    # HuggingFace Model
    hf_embedding_model: str = os.getenv("HF_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

settings = Settings()
