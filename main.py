from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant."
    ),
    (
        "human",
        "{question}"
    )
])

formatted_prompt = prompt.invoke({
    "question": "What is Python?"
})

response = llm.invoke(formatted_prompt)

print(response.content)