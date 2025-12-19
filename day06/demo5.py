from langchain.chat_models import init_chat_model
import pandas as pd
from pandasql import sqldf
import os
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openAi",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv('GROQ_API_KEY')
)

# ----- SYSTEM PROMPT (NOW USED) -----
conversation = [
    {
        "role": "system",
        "content": "You are an SQL expert."
    }
]

# ----- FIXED PATH INPUT (unicode error solved) -----
csv_file = r"C:\Users\shrey\Desktop\GenAI\IIIT_GENAI_94714\day06\employees.csv"

df = pd.read_csv(csv_file)

print("CSV Schema:")
print(df.dtypes)

while True:
    user_input = input("Ask anything about this CSV? (type exit to quit): ")
    
    # ----- FIXED EXIT CHECK -----
    if user_input.lower() == "exit":
        break

    llm_input = f"""
    You are an SQL expert.

    Table Name: data
    Table Schema: {df.dtypes}

    Question: {user_input}

    Instruction:
    Write a SQL query for the above question.
    Generate SQL query only in plain text format and nothing else.
    If you cannot generate the query, then output 'Error'.
    """

    result = llm.invoke(llm_input)
    print("\nGenerated SQL Query:")
    print(result.content)
