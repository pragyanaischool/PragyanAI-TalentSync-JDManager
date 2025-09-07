from pydantic import BaseModel, Field, HttpUrl
from typing import List

# --- Pydantic Models for API Data Validation & Serialization ---

class UrlRequest(BaseModel):
    """
    Defines the expected structure for requests that submit a URL.
    Pydantic will automatically validate that the provided 'url' is a valid HTTP/S URL.
    """
    url: HttpUrl

class QueryRequest(BaseModel):
    """
    Defines the structure for requests that query the RAG chain.
    Ensures that the 'query' is a non-empty string.
    """
    query: str = Field(..., min_length=3, max_length=500, description="The question to ask the AI.")

class SourceMetadata(BaseModel):
    """
    Defines the structure for the metadata of a source document
    that is returned along with the RAG answer.
    """
    source: str

class RAGQueryResponse(BaseModel):
    """
    Defines the shape of the JSON response from the RAG query endpoint.
    This helps in automatically generating API documentation.
    """
    answer: str
    sources: List[SourceMetadata]

class ProcessingResponseData(BaseModel):
    """
    Defines the structure of the 'data' part of a successful
    file or URL processing response.
    """
    filename: str
    size: int

class ProcessingResponse(BaseModel):
    """
    Defines the shape of the JSON response after successfully
    processing an uploaded file or a scraped URL.
    """
    message: str
    data: ProcessingResponseData
