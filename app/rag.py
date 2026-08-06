from app.retriever import hybrid_search

from app.llm import generate_answer


def build_context(chunks):

    context = ""

    for chunk in chunks:

        context += chunk.page_content

        context += "\n\n"

    return context


def ask(question):

    retrieved_chunks = hybrid_search(question)

    context = build_context(retrieved_chunks)

    answer = generate_answer(
        context=context,
        question=question
    )

    sources = list(
        dict.fromkeys(
            chunk.metadata["source"]
            for chunk in retrieved_chunks
        )
    )

    return {
        "answer": answer,
        "sources": sources,
        "chunks": retrieved_chunks
    }


if __name__ == "__main__":

    question = "What is NexusPipeline?"

    result = ask(question)

    print("=" * 60)

    print(result["answer"])

    print("=" * 60)

    print(result["sources"])


