from fastapi import APIRouter, HTTPException, UploadFile, File, status

from app.models.jd_models import UrlRequest, QueryRequest
from app.services.processing_service import process_and_embed_text
from app.core.rag_chain import rag_chain
from app.db import vector_store

router = APIRouter()

@router.post("/jds/create-from-url", status_code=status.HTTP_201_CREATED)
async def create_from_url(request: UrlRequest):
    """
    Endpoint to scrape a URL, extract text, and add it to the vector DB.
    """
    try:
        result = await process_and_embed_text(str(request.url), from_url=True)
        return {"message": "JD from URL processed successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/jds/create-from-file", status_code=status.HTTP_201_CREATED)
async def create_from_file(file: UploadFile = File(...)):
    """
    Endpoint to parse a file (PDF/DOCX), extract text, and add it to the vector DB.
    """
    if not file.content_type in [
        'application/pdf',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported file type. Please upload a PDF or DOCX."
        )
    try:
        result = await process_and_embed_text(file)
        return {"message": "JD from file processed successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/jds/query")
async def query_jds(request: QueryRequest):
    """
    Endpoint that uses the pre-built RAG chain to answer questions about the JDs.
    """
    try:
        # The .ainvoke method runs the entire RAG pipeline asynchronously
        answer = await rag_chain.ainvoke(request.query)

        # Retrieve source documents that the LLM used for its answer
        source_docs = await vector_store.as_retriever().aget_relevant_documents(request.query)

        return {
            "answer": answer,
            "sources": [doc.metadata for doc in source_docs]
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
