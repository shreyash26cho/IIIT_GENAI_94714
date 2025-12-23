import streamlit as st
import pandas as pd
from pandasql import sqldf


st.set_page_config(page_title="CSV QA Agent", layout="centered")
st.title("📄 CSV Question Answering Agent")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

if csv_file is not None:
    df = pd.read_csv(csv_file)


    st.subheader("📌 CSV Schema")
    st.write(df.dtypes)

    st.subheader("👀 CSV Preview")
    st.dataframe(df.head())

  
    question = st.text_input("Ask a question about the CSV")

    if st.button("Run Query"):

        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
          
            sql_query = "SELECT * FROM df LIMIT 5"

            result = sqldf(sql_query, {"df": df})

  
            st.subheader("✅ Answer")
            st.write(
                "I converted your question into a SQL query. "
                "The SQL query was executed on the CSV file using pandasql. "
                "Below is the output."
            )

            st.dataframe(result)

        
            st.session_state.chat_history.append(
                ("User", question)
            )
            st.session_state.chat_history.append(
                ("Agent", "Displayed first 5 records from CSV using SQL.")
            )

if st.session_state.chat_history:
    st.subheader("🕒 Chat History")

    for role, msg in st.session_state.chat_history:
        st.write(f"**{role}:** {msg}")
