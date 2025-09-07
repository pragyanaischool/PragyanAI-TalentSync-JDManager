from app.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch

# --- Database Connection ---
# Create an asynchronous client to connect to your MongoDB Atlas cluster.
# The connection string is loaded securely from the .env file via the Settings object.
client = AsyncIOMotorClient(settings.MONGO_URI)

# Get a handle to the specific database, as defined in your config.
database = client[settings.DB_NAME]

# Get a handle to the collection that will store the job descriptions.
# This single collection will hold both the text data (as 'page_content' for LangChain)
# and the vector embeddings, making it suitable for both standard queries and vector search.
jd_collection = database[settings.JD_COLLECTION_NAME]


# --- Embeddings Model Initialization ---
# This initializes the sentence-transformer model from HuggingFace.
# The model will run locally on your server to convert text documents into
# numerical vectors (embeddings). "all-MiniLM-L6-v2" is a great
# general-purpose model that balances performance and size.
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}  # Use 'cuda' if your server has a GPU for better performance
)


# --- Vector Store Initialization ---
# This object acts as the main interface for LangChain to interact with
# MongoDB Atlas for all vector-related operations. It connects the embedding model
# with the specific MongoDB collection and the vector index you've created.
vector_store = MongoDBAtlasVectorSearch(
    collection=jd_collection,
    embedding=embedding_model,
    # The 'index_name' must exactly match the name of the Vector Search Index
    # you created in the MongoDB Atlas UI.
    index_name=settings.VECTOR_INDEX_NAME
)

# This setup provides two powerful ways to interact with your data:
# 1. `jd_collection`: Use this for standard CRUD (Create, Read, Update, Delete)
#    operations on documents using the Motor driver (e.g., `await jd_collection.find_one(...)`).
# 2. `vector_store`: Use this for high-level LangChain operations like adding documents
#    with embeddings (`vector_store.aadd_texts(...)`) and performing similarity searches
#    (`vector_store.as_retriever()`).
