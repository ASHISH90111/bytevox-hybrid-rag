# ByteVox Hybrid RAG

A production-oriented Retrieval-Augmented Generation (RAG) system that answers user questions using PDF, Markdown, and Text documents. The system combines **Hybrid Retrieval (BM25 + Semantic Search + Reciprocal Rank Fusion)** with **Groq Llama 3.1** to generate grounded, context-aware responses through a FastAPI REST API.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)
![Groq](https://img.shields.io/badge/LLM-Groq-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# Project Overview

This project was developed as part of the **ByteVox AI/ML Engineering Internship Technical Assignment**.

The system implements a complete Retrieval-Augmented Generation (RAG) pipeline capable of:

- Ingesting PDF, Markdown, and Text documents
- Splitting documents into semantic chunks
- Generating embeddings using BAAI BGE Small
- Storing vectors in ChromaDB
- Performing Hybrid Retrieval
- Generating grounded answers using Groq Llama 3.1
- Exposing a REST API using FastAPI
- Logging user queries into SQLite
- Evaluating retrieval performance with benchmark questions

---

# Features

## Document Ingestion

Supported document formats:

- PDF (.pdf)
- Markdown (.md)
- Plain Text (.txt)

---

## Intelligent Chunking

- Recursive Character Text Splitter
- Chunk Size: **500**
- Chunk Overlap: **100**

---

## Embedding Model

**BAAI/bge-small-en-v1.5**

Why this model?

- Lightweight
- Fast inference
- High-quality semantic retrieval
- Open-source

---

## Vector Database

**ChromaDB**

Stores:

- Document embeddings
- Metadata
- Source filename
- Chunk IDs

---

## Hybrid Retrieval

Instead of relying only on semantic similarity, this project combines:

- Semantic Search (ChromaDB)
- BM25 Retrieval
- Reciprocal Rank Fusion (RRF)

This approach improves retrieval quality by combining semantic understanding with keyword matching.

---

## Large Language Model

**Groq API**

Model:

```
llama-3.1-8b-instant
```

Used for:

- Grounded answer generation
- Low-latency inference
- Context-aware responses

---

# System Pipeline

```text
User Question
      │
      ▼
Hybrid Retrieval
(BM25 + ChromaDB)
      │
      ▼
Reciprocal Rank Fusion
      │
      ▼
Top Retrieved Chunks
      │
      ▼
Groq Llama 3.1
      │
      ▼
Grounded Response
```

---

# REST API

Built using **FastAPI**.

## Endpoint

```
POST /query
```

Example Request

```json
{
  "question": "What is NexusPipeline?"
}
```

Example Response

```json
{
  "answer": "A directed acyclic graph (DAG) execution engine for building multi-step ML workflows...",
  "sources": [
    "01_nexus_ai_overview.txt"
  ],
  "retrieved_chunks": 5,
  "latency_ms": 421.37
}
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Evaluation

The project includes an automated evaluation framework with benchmark questions.

Current Results

| Metric | Result |
|---------|--------|
| Benchmark Questions | 5 |
| Passed | 5 |
| Retrieval Accuracy | **100%** |
| Average Latency | **~420 ms** |

Run the evaluation

```bash
python -m app.evaluation
```

---

# SQLite Logging

Every API request is automatically logged.

Logged information:

- Timestamp
- User Question
- Generated Answer
- Retrieved Sources
- Response Latency

View logs

```bash
python -m app.view_logs
```

---

# Project Structure

```text
bytevox-hybrid-rag/
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
├── architecture/
│   └── architecture.png
│
├── data/
│   └── docs/
│
├── docs/
│   ├── design_decisions.md
│   └── production_architecture.md
│
├── evaluation/
│   └── benchmark.json
│
├── main.py
├── requirements.txt
├── README.md
└── reflection.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/ASHISH90111/bytevox-hybrid-rag.git
```

Move into the project

```bash
cd bytevox-hybrid-rag
```

Create a virtual environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
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

Generate embeddings

```bash
python -m app.embeddings
```

Start the FastAPI server

```bash
uvicorn main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Technologies Used

### Backend

- Python
- FastAPI
- Uvicorn

### AI & Machine Learning

- LangChain
- HuggingFace
- BAAI BGE Small
- Groq API
- Llama 3.1 8B Instant

### Retrieval

- ChromaDB
- BM25
- Reciprocal Rank Fusion (RRF)

### Database

- SQLite
- ChromaDB

### Document Processing

- PyMuPDF
- Markdown

---

# Assignment Deliverables

- ✅ PDF, Markdown and TXT document support
- ✅ Hybrid Retrieval (BM25 + Semantic Search + RRF)
- ✅ FastAPI REST API
- ✅ Evaluation Framework
- ✅ Design Decisions Document
- ✅ Production Architecture Document
- ✅ Architecture Diagram
- ✅ Reflection Write-up
- ✅ SQLite Query Logging (Bonus)

---

# Documentation

| File | Description |
|------|-------------|
| README.md | Project setup and usage |
| docs/design_decisions.md | Engineering design decisions |
| docs/production_architecture.md | Production-ready architecture |
| architecture/architecture.png | Architecture diagram |
| reflection.md | Assignment reflection |

---

# Future Improvements

- Cross-Encoder Reranking
- Query Expansion
- Redis Cache
- Streaming Responses
- User Authentication
- Monitoring Dashboard

---

# Author

**Ashish**

B.Tech, National Institute of Technology (NIT) Jalandhar

Developed as part of the **ByteVox AI/ML Engineering Internship Technical Assignment**.
