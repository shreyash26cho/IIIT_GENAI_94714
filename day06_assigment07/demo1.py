from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy",
    model="meta-llama-3.1-8b-instruct"
)

user_input = input("You: ")

for chunk in llm.stream(user_input):
    print(chunk.content, end="")
