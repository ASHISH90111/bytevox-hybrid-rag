import time

from fastapi import FastAPI
from pydantic import BaseModel

from app.logger import (
    initialize_database,
    log_query
)

from app.rag import ask

# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="ByteVox RAG API",
    version="1.0.0"
)

# Create SQLite database if it doesn't exist
initialize_database()


# =====================================================
# Request Model
# =====================================================

class QueryRequest(BaseModel):
    question: str


# =====================================================
# Response Model
# =====================================================

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    retrieved_chunks: int
    latency_ms: float


# =====================================================
# Home Endpoint
# =====================================================

@app.get("/")
def home():
    return {
        "message": "ByteVox RAG API Running"
    }


# =====================================================
# Query Endpoint
# =====================================================

@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):

    start = time.perf_counter()

    result = ask(request.question)

    latency = round(
        (time.perf_counter() - start) * 1000,
        2
    )

    log_query(
        question=request.question,
        answer=result["answer"],
        sources=result["sources"],
        latency=latency
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"],
        "retrieved_chunks": len(result["chunks"]),
        "latency_ms": latency
    }