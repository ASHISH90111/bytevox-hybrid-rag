from groq import Groq

from app.config import (
    GROQ_API_KEY,
    GROQ_MODEL
)

client = Groq(
    api_key=GROQ_API_KEY
)


def build_prompt(context, question):

    return f"""
You are an AI assistant.

Answer ONLY using the provided context.

If the answer is not contained in the context,
reply:

"I couldn't find that information in the documents."

Context
------------------

{context}

------------------

Question:

{question}

Answer:
"""

def generate_answer(context, question):

    prompt = build_prompt(
        context,
        question
    )

    response = client.chat.completions.create(

        model=GROQ_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0,

        max_tokens=512
    )

    return response.choices[0].message.content