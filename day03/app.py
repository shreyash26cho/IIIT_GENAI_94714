import streamlit as st
import pandas as pd
import pandasql as ps

st.title("CSV SQL Executor")

# Upload CSV file
file = st.file_uploader("book_hdr", type=["csv"])

# Check if file is uploaded
if file is not None:
    try:
        # Read CSV file
        df = pd.read_csv(file)
        st.subheader("Uploaded CSV Data")
        st.dataframe(df)

        # SQL query input
        query = st.text_area("Enter SQL Query (use table name: data)")

        # Run SQL query
        if st.button("Run Query"):
            result = ps.sqldf(query, {"data": df})
            st.subheader("Query Result")
            st.dataframe(result)

    except Exception as e:
        st.error(f"Error: {e}")
