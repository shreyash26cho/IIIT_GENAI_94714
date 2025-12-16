import streamlit as st
import pandas as pd
import pandasql as ps

st.title("CSV SQL Executor")


if "page" not in st.session_state:
    st.session_state.page = "input"

if "result" not in st.session_state:
    st.session_state.result = None


if st.session_state.page == "input":

    file = st.file_uploader("book_hdr", type=["csv"])

    if file is not None:
        try:
            df = pd.read_csv(file)
            st.subheader("Uploaded CSV Data")
            st.dataframe(df)

            query = st.text_area("Enter SQL Query (use table name: data)")

            if st.button("Run Query"):
                result = ps.sqldf(query, {"data": df})
                st.session_state.result = result
                st.session_state.page = "result"  

        except Exception as e:
            st.error(f"Error: {e}")


elif st.session_state.page == "result":

    st.subheader("Query Result (New Page)")
    st.dataframe(st.session_state.result)

    if st.button("Back"):
        st.session_state.page = "input"
