import streamlit as st
from langchain_openai import ChatOpenAI
import os

st.title("LangChain + LM Studio Chat")

# Initialize model
llm = ChatOpenAI (
    base_url="https://api.groq.com/openai/v1",
    api_key='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',
    model="meta-llama-3.1-8b-instruct"
)


user_input = st.chat_input("Say something...")

# Streaming response
if user_input:
    st.write("**AI:**")
    st.write_stream(
        (chunk.content for chunk in llm.stream(user_input))
    )
