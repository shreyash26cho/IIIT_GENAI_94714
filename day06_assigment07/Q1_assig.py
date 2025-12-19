import streamlit as st
import pandas as pd
from pandasql import sqldf
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Initialize LLM
llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("CSV SQL Chatbot")

# CSV file path
csv_file = r"C:\Users\shrey\Desktop\GenAI\IIIT_GENAI_94714\day06_assigment07\employees.csv"

# ✅ FIX: use csv_file instead of file
if csv_file:
    df = pd.read_csv(csv_file)

    st.subheader("CSV Schema")
    st.write(df.dtypes)

    st.subheader("Preview")
    st.dataframe(df.head())

    # User question
    question = st.text_input("Ask a question:")

    if st.button("Run") and question:

        # Convert question to SQL
        prompt = f"""
        Table name: data
        Schema:
        {df.dtypes}

        Question:
        {question}

        Write only SQL.
        """

        sql = llm.invoke(prompt).content.strip()

        st.subheader("SQL Query")
        st.code(sql, language="sql")

        try:
            # Run SQL on CSV
            result = sqldf(sql, {"data": df})

            st.subheader("Result")
            st.dataframe(result)

            # Explain result
            explain = llm.invoke(
                f"Explain this result in simple English:\n{result.head()}"
            ).content

            st.subheader("Explanation")
            st.write(explain)

        except Exception as e:
            st.error(f"Invalid SQL query: {e}")
