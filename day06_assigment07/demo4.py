from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    conversation.append({"role": "user", "content": user_input})

    response = llm.invoke(conversation)
    print("AI:", response.content)

    conversation.append({"role": "assistant", "content": response.content})
