from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key='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'
)

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = llm.invoke(conversation)
    print("AI:", response.content)

    conversation.append({
        "role": "assistant",
        "content": response.content
    })
