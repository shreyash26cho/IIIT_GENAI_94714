import streamlit as st
import requests
import json
import os
import time


st.set_page_config(page_title="Multi-LLM Chatbot", layout="centered")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.sidebar.title("🔧 Model Settings")

model_choice = st.sidebar.selectbox(
    "Select Model",
    ["Groq (Cloud)", "LM Studio (Local)"]
)

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

def groq_response(user_input):
    api_key = os.getenv("GROQ_API_KEY")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {'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'}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]


def local_response(user_input):
    url = "http://127.0.0.1:1234/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer demo_api"   # ignored by LM Studio
    }

    data = {
        "model": "meta-llama-3.1-8b-instruct",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["choices"][0]["message"]["content"]


st.title("🤖 Multi-LLM Chatbot")
st.caption("Groq Cloud + LM Studio Local")

user_input = st.text_input("Ask your question:")

if st.button("Send"):
    if user_input.strip() != "":
        start_time = time.perf_counter()

        if model_choice == "Groq (Cloud)":
            answer = groq_response(user_input)
        else:
            answer = local_response(user_input)

        end_time = time.perf_counter()

        st.session_state.chat_history.append({
            "user": user_input,
            "bot": answer,
            "model": model_choice,
            "time": f"{end_time - start_time:.2f} sec"
        })


st.subheader("💬 Chat History")

for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**{chat['model']}:** {chat['bot']}")
    st.markdown(f"_Response Time: {chat['time']}_")
    st.markdown("---")
