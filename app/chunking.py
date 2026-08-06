from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)

def split_documents(documents):

    chunks = text_splitter.split_documents(documents)

    for idx, chunk in enumerate(chunks):

        chunk.metadata["chunk_id"] = idx

    return chunks

if __name__ == "__main__":

    from app.ingestion import load_documents

    docs = load_documents()

    chunks = split_documents(docs)

    print("=" * 60)
    print(f"Total Chunks : {len(chunks)}")
    print("=" * 60)

    for chunk in chunks[:5]:

        print(chunk.metadata)
        print(chunk.page_content[:200])
        print("-" * 60)