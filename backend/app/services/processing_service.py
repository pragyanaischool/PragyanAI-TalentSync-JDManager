import requests
from bs4 import BeautifulSoup
from fastapi import UploadFile
import PyPDF2
import docx
import io
from app.db import vector_store

def _scrape_url_text(url: str) -> str:
    """Scrapes the visible text content from a given URL."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        # Remove script and style elements for cleaner text
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        return soup.get_text(separator=' ', strip=True)
    except requests.RequestException as e:
        print(f"Error scraping URL {url}: {e}")
        raise

def _extract_text_from_pdf(file_stream: io.BytesIO) -> str:
    """Extracts text from a PDF file stream."""
    reader = PyPDF2.PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def _extract_text_from_docx(file_stream: io.BytesIO) -> str:
    """Extracts text from a DOCX file stream."""
    doc = docx.Document(file_stream)
    # Concatenate all paragraphs separated by newline
    return "\n".join([para.text for para in doc.paragraphs])


async def process_and_embed_text(source, from_url: bool = False):
    """
    Processes text from a URL or an uploaded file, then adds it to the vector store.

    :param source: URL string if from_url=True, otherwise an UploadFile instance
    :param from_url: Flag indicating if source is a URL or file
    :return: dict with filename/source and extracted text size
    """
    text_content = ""
    metadata = {}

    if from_url:
        text_content = _scrape_url_text(source)
        metadata = {"source": source}
    else:  # It's an UploadFile
        file_stream = io.BytesIO(await source.read())
        if source.content_type == 'application/pdf':
            text_content = _extract_text_from_pdf(file_stream)
        elif source.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            text_content = _extract_text_from_docx(file_stream)
        else:
            raise ValueError(f"Unsupported file type: {source.content_type}")
        metadata = {"source": source.filename}

    if not text_content.strip():
        raise ValueError("No text content could be extracted from the source.")

    # Add the extracted text and metadata to the vector store using LangChain method
    await vector_store.aadd_texts([text_content], metadatas=[metadata])

    return {"filename": metadata["source"], "size": len(text_content)}
