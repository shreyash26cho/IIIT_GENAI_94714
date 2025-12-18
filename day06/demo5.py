from langchain.chat_models import init_chat_model
import pandas as pd

llm=init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openAi",
    base_url="https://api.groq.com/openai/v1",
    api_key='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'

)
conversation = [
    {
        "role": "system",
        "content": "You are an SQL expert."
    }
]

csv_file=input("C:\Users\shrey\Desktop\GenAI\IIIT_GENAI_94714\day06\employees.csv")
df=pd.read_csv(csv_file)
print("csv scheme :")
print(df.dtypes)


while True:
    user_input = input("Ask anything about this CSV? ")
    if user_input == "exit":
        break
    llm_input = f"""
        Table Name: data
        Table Schema: {df.dtypes}
        Question: {user_input}
        Instruction:
            Write a SQL query for the above question. 
            Generate SQL query only in plain text format and nothing else.
            If you cannot generate the query, then output 'Error'.
    """
    result = llm.invoke(llm_input)
    print(result.content)




