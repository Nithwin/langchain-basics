from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.

Context:
{context}

Question:
{question}

Answer:
"""
)

formatted_prompt = prompt.invoke(
    {
        "context": "Python is a programming language.",
        "question": "What is Python?"
    }
)

print(formatted_prompt)