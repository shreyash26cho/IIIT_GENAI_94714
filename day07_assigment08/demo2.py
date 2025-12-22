from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """Calculator tool to evaluate math expressions"""
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error: Cannot solve expression"


llm = init_chat_model(
    model="google/gemma-3n-e4b",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="non-needed"
)


conversation = []

agent = create_agent(
    model=llm,
    tools=[calculator],
    system_prompt="You are a helpful assistant. Use calculator for math. Answer in short."
)


while True:
    user_input = input("You: ")
    if user_input == "exit":
        break

    conversation.append({"role": "user", "content": user_input})

    result = agent.invoke({"messages": conversation})

    ai_msg = result["messages"][-1]
    print("AI:", ai_msg.content)

    conversation = result["messages"]
