from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import jd_router

# Create the FastAPI application instance
app = FastAPI(
    title="JD Management & Intelligence API",
    description="API for processing and querying job descriptions using RAG.",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows your React frontend (running on a different domain/port) to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    # In production, replace "*" with your frontend's actual URL(s)
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include the API router from the jd_router module
# All routes defined in jd_router will be prefixed with /api
app.include_router(jd_router.router, prefix="/api")

# A simple root endpoint to confirm the API is running
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the JD Management API"}

# To run this application locally:
# 1. Ensure your .env file is correctly set up with all required environment variables.
# 2. In your terminal, run: uvicorn main:app --reload
