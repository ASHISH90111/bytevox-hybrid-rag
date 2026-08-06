from pathlib import Path

import pymupdf
from langchain_core.documents import Document

from app.config import DOCUMENTS_DIR

def load_txt(file_path: Path):
    """
    Load a plain text file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return [
        Document(
            page_content=text,
            metadata={
                "source": file_path.name,
                "page": 0
            }
        )
    ]

def load_markdown(file_path: Path):
    """
    Load a markdown file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return [
        Document(
            page_content=text,
            metadata={
                "source": file_path.name,
                "page": 0
            }
        )
    ]


def load_pdf(file_path):
    """
    Load every page from a PDF file.
    """

    pdf = pymupdf.open(file_path)

    documents = []

    for page_number, page in enumerate(pdf):

        text = page.get_text()

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file_path.name,
                    "page": page_number + 1,
                },
            )
        )

    pdf.close()

    return documents

def load_documents():

    documents = []

    for file in DOCUMENTS_DIR.iterdir():

        suffix = file.suffix.lower()

        if suffix == ".txt":
            documents.extend(load_txt(file))

        elif suffix == ".md":
            documents.extend(load_markdown(file))

        elif suffix == ".pdf":
            documents.extend(load_pdf(file))

    return documents

if __name__ == "__main__":

    docs = load_documents()

    print("=" * 60)
    print(f"Loaded {len(docs)} Documents")
    print("=" * 60)

    for doc in docs:

        print(doc.metadata)

        print(doc.page_content[:120])

        print("-" * 60)