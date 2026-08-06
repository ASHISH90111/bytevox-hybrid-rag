# Reflection

## 1. What was the most difficult engineering decision you made?

The most challenging engineering decision was selecting the retrieval strategy. A simple vector similarity search was straightforward to implement, but it could miss documents containing exact technical keywords. On the other hand, BM25 performs well for keyword matching but lacks semantic understanding. I chose a hybrid retrieval approach combining BM25, semantic vector search using ChromaDB, and Reciprocal Rank Fusion (RRF). This decision improved retrieval quality by leveraging the strengths of both lexical and semantic search while keeping the implementation modular and easy to extend.

---

## 2. What would you improve with an additional week?

With an additional week, I would enhance the system by adding a cross-encoder reranker to improve document ranking accuracy. I would also implement query expansion for better handling of short or ambiguous questions, introduce Redis caching to reduce response latency, and containerize the application using Docker for easier deployment. Additionally, I would build an evaluation dashboard to visualize retrieval metrics, latency, and benchmark performance in real time.

---

## 3. What part of the stack would you like to learn more about?

I would like to deepen my understanding of production-scale LLM infrastructure and distributed retrieval systems. Specifically, I want to learn more about deploying vector databases such as Qdrant or Weaviate in Kubernetes environments, implementing efficient caching strategies, and building highly available, scalable RAG systems that serve thousands of concurrent users with low latency.

---

## 4. How did AI tools help you during implementation?

AI tools significantly accelerated development by assisting with code generation, debugging, library documentation, and implementation ideas. They helped identify errors quickly, explain framework behavior, and suggest improvements to the overall architecture. I used AI as an engineering assistant to iterate faster while verifying the generated code, adapting it to the project requirements, and making design decisions based on performance, maintainability, and production readiness.