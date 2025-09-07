from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel
from app.config import settings

def get_llm() -> BaseChatModel:
    """
    Factory function to select and instantiate the language model.

    Reads the LLM_PROVIDER from the application settings and returns the
    corresponding LangChain chat model instance, configured with the
    appropriate API key and model name.
    """
    provider = settings.LLM_PROVIDER.lower()

    if provider == "groq":
        if not settings.GROQ_API_KEY:
            raise ValueError("LLM_PROVIDER is set to 'groq' but GROQ_API_KEY is missing in .env")
        return ChatGroq(
            model_name=settings.GROQ_MODEL_NAME,
            api_key=settings.GROQ_API_KEY,
            temperature=0  # Setting to 0 for more deterministic and factual responses
        )
    
    elif provider == "openai":
        if not settings.OPENAI_API_KEY:
            raise ValueError("LLM_PROVIDER is set to 'openai' but OPENAI_API_KEY is missing in .env")
        return ChatOpenAI(
            model_name=settings.OPENAI_MODEL_NAME,
            api_key=settings.OPENAI_API_KEY,
            temperature=0
        )
        
    # This is where you could easily add more providers in the future.
    # For example:
    # elif provider == "anthropic":
    #     # return ChatAnthropic(...)
    #     pass
        
    else:
        raise ValueError(
            f"Unsupported LLM provider: '{provider}'. "
            "Please check the LLM_PROVIDER value in your .env file. "
            "Supported options are 'groq' or 'openai'."
        )

# Create a single, importable instance of the LLM for the entire application to use.
# This ensures that the model is initialized only once.
llm = get_llm()
