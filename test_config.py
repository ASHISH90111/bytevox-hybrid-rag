from app.config import *

print("=" * 50)
print("Project Root")
print(BASE_DIR)

print("=" * 50)
print("Documents")
print(DOCUMENTS_DIR)

print("=" * 50)
print("Chroma")
print(CHROMA_DB_DIR)

print("=" * 50)
print("Embedding Model")
print(EMBEDDING_MODEL)

print("=" * 50)
print("Chunk Size")
print(CHUNK_SIZE)

print("=" * 50)
print("Chunk Overlap")
print(CHUNK_OVERLAP)

print("=" * 50)
print("Vector Top K")
print(TOP_K_VECTOR)

print("=" * 50)
print("BM25 Top K")
print(TOP_K_BM25)

print("=" * 50)
print("Final Retrieved")
print(FINAL_TOP_K)