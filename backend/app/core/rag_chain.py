from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.db import vector_store
from app.core.llm_provider import llm

# --- RAG Prompt Template ---
# This template is crucial for instructing the LLM on how to behave.
# It explicitly tells the model to answer *only* based on the provided context,
# which helps prevent it from making up information ("hallucinating").
prompt_template = """
You are an expert assistant for analyzing job descriptions.
Answer the user's question based *only* on the following context.
If the information to answer the question is not in the context, clearly state that you cannot find the answer in the provided documents.
Do not make up information.

Context:
{context}

Question:
{question}
"""
prompt = ChatPromptTemplate.from_template(prompt_template)

# --- RAG Chain Definition ---

def format_docs(docs):
    """
    A helper function to combine the content of multiple retrieved documents
    into a single string, separated for clarity.
    """
    return "\n\n---\n\n".join(doc.page_content for doc in docs)

# This is the main RAG chain, constructed using the LangChain Expression Language (LCEL).
# The '|' (pipe) operator chains together different components, passing the output
# of one step as the input to the next.
rag_chain = (
    {
        # The retriever fetches relevant documents from the vector store based on the user's question.
        # The result is then formatted by our `format_docs` function.
        "context": vector_store.as_retriever() | format_docs,
        # `RunnablePassthrough` ensures the original question is passed along to the next step.
        "question": RunnablePassthrough()
    }
    | prompt          # The context and question are formatted by the prompt template.
    | llm             # The formatted prompt is sent to the selected LLM (from llm_provider).
    | StrOutputParser() # The LLM's response object is parsed into a simple string.
)
