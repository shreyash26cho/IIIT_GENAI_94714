import streamlit as st
from langchain.chat_models import init_chat_model
import os



st.title("langchain_model")
llm =init_chat_model(
   model="meta-llama-3.1-8b-instruct",
   model_provider="openai",
   base_url="http://127.0.0.1:1234/v1",
   api_key=os.getenv('')

)

user_input=st.chat_input("say something")
if user_input:
    result=llm.stream(user_input)

st.write_stream([chunk.content for chunk in result])   

