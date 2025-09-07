from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Centralized app settings loaded from `.env` and environment variables,
    with validation and default values.
    """

    # Configuration to load from .env file with UTF-8 encoding
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'  # ignore unexpected env vars gracefully
    )

    # Backend / Frontend CORS origins as a list (comma-separated string supported)
    frontend_origins: list[str] = ["*"]

    # MongoDB connection and collections
    mongo_uri: str
    mongo_db_name: str = "jddatabase"
    mongo_collection_name: str = "jds"
    mongo_vector_collection_name: str = "vector_index"

    # LLM Provider and API keys
    llm_provider: str = "groq"
    groq_api_key: str | None = None
    openai_api_key: str | None = None

    # Model specification for providers
    groq_model_name: str = "llama3-8b-8192"
    openai_model_name: str = "gpt-4o-mini"

    # HuggingFace Embedding model
    hf_embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Override default validator to split frontend_origins if provided as a string
    @classmethod
    def model_post_parse(cls, values: dict) -> dict:
        origins = values.get("frontend_origins")
        if isinstance(origins, str):
            values["frontend_origins"] = [o.strip() for o in origins.split(",")]
        return values

# Single instance for import everywhere
settings = Settings()
