# Design Decisions

## Overview

This document explains the key engineering decisions made while building the ByteVox Retrieval-Augmented Generation (RAG) system. The focus was on creating a solution that is simple, modular, easy to understand, and suitable for production with minimal changes.

---

# 1. Vector Database Selection

## Selected Vector Database

**ChromaDB**

### Why ChromaDB?

ChromaDB was selected because it provides a lightweight and developer-friendly vector database that integrates seamlessly with LangChain. Since this project is intended as a technical assignment, ChromaDB allows rapid development without requiring additional infrastructure or external services.

The database stores vector embeddings together with metadata such as document source, page number, and chunk ID, enabling efficient retrieval and traceability of generated answers.

### Advantages

- Simple local deployment
- No external server required
- Excellent LangChain integration
- Persistent local storage
- Fast similarity search
- Easy metadata filtering
- Suitable for small to medium document collections

### Alternatives Considered

### FAISS

**Pros**

- Extremely fast similarity search
- Low memory overhead
- Mature library

**Cons**

- No built-in metadata storage
- Additional code required for persistence
- Less convenient integration with LangChain metadata

---

### Pinecone

**Pros**

- Fully managed cloud service
- Automatic scaling
- High availability

**Cons**

- Requires cloud account
- Usage costs increase with scale
- Unnecessary complexity for this assignment

---

### Qdrant

**Pros**

- Excellent filtering capabilities
- Production ready
- Distributed architecture

**Cons**

- Requires running an additional server
- More operational overhead

---

### Why Chroma Was Chosen

For a technical assignment focused on engineering decisions rather than infrastructure, ChromaDB provides the best balance between simplicity, performance, persistence, and ease of integration.

---

# 2. Embedding Model Selection

## Selected Model

**BAAI/bge-small-en-v1.5**

### Why This Model?

The BGE Small embedding model provides high-quality semantic representations while remaining computationally efficient. It performs well on retrieval benchmarks and generates normalized embeddings that work effectively with cosine similarity.

Compared to larger embedding models, it offers significantly lower inference time and memory usage while maintaining strong retrieval quality.

### Advantages

- Open-source
- Fast embedding generation
- Low memory footprint
- Excellent semantic retrieval quality
- Well supported in LangChain
- Optimized for retrieval tasks

### Alternatives Considered

### OpenAI Embeddings

**Pros**

- Very high quality
- Strong multilingual performance

**Cons**

- Paid API
- Internet dependency
- Vendor lock-in

---

### Sentence Transformers (all-MiniLM)

**Pros**

- Lightweight
- Fast inference

**Cons**

- Slightly lower retrieval quality than BGE Small

---

### bge-large

**Pros**

- Higher retrieval accuracy

**Cons**

- Larger model size
- Increased inference latency
- Higher RAM requirements

---

### Trade-offs

Choosing BGE Small prioritizes efficiency and fast inference while maintaining strong semantic retrieval quality. It provides an excellent balance for a lightweight production-ready RAG system.

---

# 3. Chunking Strategy

## Chunk Size

**500 characters**

### Chunk Overlap

**100 characters**

### Why These Values?

The chosen chunk size balances retrieval precision with contextual completeness.

Smaller chunks improve retrieval specificity but may lose important surrounding context. Larger chunks preserve more context but increase irrelevant information passed to the language model.

An overlap of 100 characters ensures that information located near chunk boundaries is preserved across adjacent chunks, reducing the chance of missing relevant context.

### Advantages

- Better semantic retrieval
- Reduced context fragmentation
- Lower token usage compared to larger chunks
- Improved answer grounding

### Trade-offs

| Smaller Chunks | Larger Chunks |
|---------------|---------------|
| Better precision | More context |
| Less token usage | Higher token cost |
| More chunks to index | Fewer chunks |
| Risk of losing context | Risk of retrieving irrelevant text |

The selected values provide a practical balance between retrieval quality, latency, and token efficiency.

---

# 4. Retrieval Strategy

A hybrid retrieval approach was implemented instead of relying solely on vector similarity.

The retrieval pipeline consists of:

1. Semantic Search using ChromaDB embeddings
2. BM25 lexical retrieval
3. Reciprocal Rank Fusion (RRF) to combine rankings

### Why Hybrid Retrieval?

Semantic retrieval captures conceptual similarity but may overlook exact keywords or technical terms.

BM25 excels at exact keyword matching but cannot understand semantic relationships.

Combining both approaches improves recall and retrieval robustness, especially for technical documentation containing APIs, version numbers, and configuration terms.

---

# 5. Overall Engineering Trade-offs

| Decision | Reason |
|----------|--------|
| ChromaDB | Lightweight, persistent, easy integration |
| BGE Small | Fast, efficient, high-quality embeddings |
| Hybrid Retrieval | Better accuracy than semantic search alone |
| Chunk Size 500 | Good balance between precision and context |
| Overlap 100 | Preserves information across chunk boundaries |
| Groq Llama 3.1 | Fast inference with low latency |
| FastAPI | Simple, modern REST API framework |

---

# Conclusion

The overall design prioritizes simplicity, modularity, retrieval quality, and maintainability while remaining suitable for future production deployment. Hybrid retrieval, efficient embeddings, and structured document chunking together provide accurate grounded responses with low latency. These design choices enable the system to scale with minimal architectural changes while keeping the implementation understandable and easy to extend.