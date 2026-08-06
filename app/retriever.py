from rank_bm25 import BM25Okapi

from app.ingestion import load_documents
from app.chunking import split_documents
from app.embeddings import search

documents = load_documents()

chunks = split_documents(documents)


tokenized_chunks = [
    chunk.page_content.lower().split()
    for chunk in chunks
]


bm25 = BM25Okapi(tokenized_chunks)


def bm25_search(query, k=10):

    tokens = query.lower().split()

    scores = bm25.get_scores(tokens)

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        doc
        for doc, score in ranked[:k]
    ]


def vector_search(query, k=10):

    return search(query, k)


def reciprocal_rank_fusion(
    vector_results,
    bm25_results,
    k=60
):

    scores = {}

    for rank, doc in enumerate(vector_results):

        key = (
            doc.metadata["source"],
            doc.metadata["chunk_id"]
        )

        scores[key] = scores.get(key, 0) + 1 / (k + rank + 1)

    for rank, doc in enumerate(bm25_results):

        key = (
            doc.metadata["source"],
            doc.metadata["chunk_id"]
        )

        scores[key] = scores.get(key, 0) + 1 / (k + rank + 1)

    lookup = {}

    for doc in vector_results + bm25_results:

        key = (
            doc.metadata["source"],
            doc.metadata["chunk_id"]
        )

        lookup[key] = doc

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        lookup[key]
        for key, score in ranked[:5]
    ]


def hybrid_search(query):

    vector = vector_search(query)

    bm = bm25_search(query)

    return reciprocal_rank_fusion(
        vector,
        bm
    )

if __name__ == "__main__":

    query = "What is NexusPipeline?"

    print("=" * 60)
    print("VECTOR")
    print("=" * 60)

    vector = vector_search(query)

    for doc in vector[:3]:

        print(doc.metadata)

    print()

    print("=" * 60)
    print("BM25")
    print("=" * 60)

    bm = bm25_search(query)

    for doc in bm[:3]:

        print(doc.metadata)

    print()

    print("=" * 60)
    print("HYBRID")
    print("=" * 60)

    hybrid = hybrid_search(query)

    for doc in hybrid:

        print(doc.metadata)




