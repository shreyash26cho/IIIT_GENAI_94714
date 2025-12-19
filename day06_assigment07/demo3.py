from langchain_openai import ChatOpenAI

# Initialize LM Studio model
llm = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy",  # LM Studio does not need real key
    model="meta-llama-3.1-8b-instruct"
)

conversation = list([])

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # add user message
    conversation.append({
        "role": "user",
        "content": user_input
    })

    # get response
    llm_output = llm.invoke(conversation)
    print("AI:", llm_output.content)

    # add assistant message
    conversation.append({
        "role": "assistant",
        "content": llm_output.content
    })
