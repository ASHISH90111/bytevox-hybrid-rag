from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from app.config import (
    EMBEDDING_MODEL,
    CHROMA_DB_DIR,
    COLLECTION_NAME,
    DEVICE,
)

embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL,
    model_kwargs={
        "device": DEVICE
    },
    encode_kwargs={
        "normalize_embeddings": True
    }
)

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embedding_model,
    persist_directory=str(CHROMA_DB_DIR)
)

def index_documents(chunks):
    """
    Clear existing collection and index fresh documents.
    """

    vector_store.reset_collection()

    vector_store.add_documents(chunks)

    print(f"\nIndexed {len(chunks)} chunks successfully.")


def search(query, k=5):

    results = vector_store.similarity_search(
        query=query,
        k=k
    )

    return results


if __name__ == "__main__":

    from app.ingestion import load_documents
    from app.chunking import split_documents

    print("=" * 60)
    print("Loading documents...")
    print("=" * 60)

    docs = load_documents()

    chunks = split_documents(docs)

    index_documents(chunks)

    print("=" * 60)
    print("Testing Search")
    print("=" * 60)

    results = search(
        "What is NexusPipeline?"
    )

    for i, doc in enumerate(results, start=1):

        print(f"\nResult {i}")

        print(doc.metadata)

        print(doc.page_content[:250])