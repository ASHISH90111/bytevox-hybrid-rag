# ByteVox AI/ML Engineering Technical Assignment

A production-oriented Retrieval-Augmented Generation (RAG) system that answers user questions using a collection of documents. The system combines semantic retrieval with lexical retrieval (Hybrid Search) and exposes the functionality through a FastAPI REST API.


# ByteVox Hybrid RAG

![Python](https://img.shields.io/badge/Python-3.11-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)

![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)

![Groq](https://img.shields.io/badge/LLM-Groq-red)

![License](https://img.shields.io/badge/license-MIT-blue)

---

# Project Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline capable of:

- Ingesting PDF, Markdown, and Text documents
- Splitting documents into semantic chunks
- Generating embeddings using BAAI BGE Small
- Storing vectors in ChromaDB
- Performing Hybrid Retrieval using:
  - Semantic Search
  - BM25
  - Reciprocal Rank Fusion (RRF)
- Generating grounded answers using Groq Llama 3.1
- Exposing a REST API with FastAPI
- Logging queries into SQLite
- Evaluating retrieval performance using benchmark questions

---

# Features

## Document Ingestion

Supports

- PDF
- Markdown (.md)
- Plain Text (.txt)

---

## Intelligent Chunking

- Recursive Character Text Splitter
- Chunk Size: 500 characters
- Chunk Overlap: 100 characters

---

## Embedding Model

Model

BAAI/bge-small-en-v1.5

Features

- Lightweight
- Fast inference
- High-quality semantic embeddings
- Normalized embeddings

---

## Vector Database

ChromaDB

Stores

- Document embeddings
- Metadata
- Source information
- Chunk IDs

---

## Hybrid Retrieval

Instead of relying only on semantic search, this project combines

- BM25 Retrieval
- Embedding Retrieval
- Reciprocal Rank Fusion (RRF)

This improves retrieval quality by combining lexical matching with semantic similarity.

---

## Large Language Model

Groq API

Model

llama-3.1-8b-instant

Used for

- Grounded answer generation
- Low-latency inference
- Context-aware responses

---

## REST API

Implemented using FastAPI.

Endpoint

POST

```
/query
```

Example Request

```json
{
    "question":"What is NexusPipeline?"
}
```

Example Response

```json
{
    "answer":"A directed acyclic graph (DAG) execution engine...",
    "sources":[
        "01_nexus_ai_overview.txt"
    ],
    "retrieved_chunks":5,
    "latency_ms":420.35
}
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Evaluation

Evaluation includes

- 5 benchmark questions
- Retrieval accuracy
- Expected source verification
- Average response latency

Current Results

| Metric | Value |
|----------|---------|
| Benchmark Questions | 5 |
| Passed | 5 |
| Retrieval Accuracy | 100% |
| Average Latency | ~420 ms |

---

## Logging

SQLite logging records

- Timestamp
- User Question
- Generated Answer
- Retrieved Sources
- Response Latency

---

# Project Structure

```
bytevox-hybrid-rag

│
├── app/
│   ├── api.py
│   ├── chunking.py
│   ├── config.py
│   ├── embeddings.py
│   ├── evaluation.py
│   ├── ingestion.py
│   ├── llm.py
│   ├── logger.py
│   ├── rag.py
│   ├── retriever.py
│   └── view_logs.py
│
├── data/
│   ├── docs/
│   └── chroma_db/
│
├── evaluation/
│   └── benchmark.json
│
├── requirements.txt
│
├── main.py
│
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/ASHISH90111/bytevox-hybrid-rag.git
```

Move into the project

```bash
cd bytevox-rag
```

Create virtual environment

Windows

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# Running the Project

## Step 1

Generate embeddings

```bash
python -m app.embeddings
```

---

## Step 2

Start FastAPI

```bash
uvicorn main:app --reload
```

---

## Step 3

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# Running Evaluation

```bash
python -m app.evaluation
```

Example Output

```
Accuracy : 100%

Average Latency : 421 ms
```

---

# Viewing Logs

```bash
python -m app.view_logs
```

---

# Technologies Used

## Backend

- Python 3.11
- FastAPI
- Uvicorn

---

## AI & Machine Learning

- LangChain
- HuggingFace
- BAAI BGE Small
- Groq API
- Llama 3.1 8B Instant

---

## Retrieval

- ChromaDB
- BM25
- Reciprocal Rank Fusion

---

## Database

- SQLite
- ChromaDB

---

## Document Processing

- PyMuPDF
- Markdown
- LangChain Document Loader

---

## Evaluation

- Benchmark Questions
- Retrieval Accuracy
- Response Latency

---

# Future Improvements

- Cross-Encoder Reranking
- Query Expansion
- Streaming Responses
- Redis Cache
- Kubernetes Deployment
- Multi-user Authentication
- Dashboard for Retrieval Metrics

---

# Assignment Coverage

| Requirement | Status |
|-------------|---------|
| PDF Support | ✅ |
| Markdown Support | ✅ |
| TXT Support | ✅ |
| Hybrid Retrieval | ✅ |
| REST API | ✅ |
| Evaluation Script | ✅ |
| Design Document | ✅ |
| Architecture | ✅ |
| Reflection | ✅ |
| SQLite Logging | ✅ Bonus |

---

# Author

Ashish

NIT Jalandhar

AI/ML Engineering Internship Assignment – ByteVox
