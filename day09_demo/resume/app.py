import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI

# ---------------- LOAD ENV ----------------
load_dotenv()

st.set_page_config(page_title="Resume Q&A (No Chunking)", layout="wide")
st.title("📄 Resume Question Answering (Prompt-Based)")

# ---------------- LOAD RESUMES ----------------
RESUME_FOLDER = "resumes"

RESUME_PATHS = [
    r"C:\Users\shrey\Desktop\GenAI\IIIT_GENAI_94714\day09_demo\resume\resume-001.pdf",
    r"C:\Users\shrey\Desktop\GenAI\IIIT_GENAI_94714\day09_demo\resume\resume-002.pdf",
    r"C:\Users\shrey\Desktop\GenAI\IIIT_GENAI_94714\day09_demo\resume\resume-003.pdf",
]

if not os.path.exists(RESUME_FOLDER):
    os.makedirs(RESUME_FOLDER)

all_text = ""

# load from folder
for file in os.listdir(RESUME_FOLDER):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(RESUME_FOLDER, file))
        docs = loader.load()
        for d in docs:
            all_text += d.page_content + "\n\n"

# load from absolute paths
for path in RESUME_PATHS:
    if os.path.exists(path):
        loader = PyPDFLoader(path)
        docs = loader.load()
        for d in docs:
            all_text += d.page_content + "\n\n"
    else:
        st.warning(f"Resume not found: {path}")

if all_text.strip() == "":
    st.warning("No PDF resumes found.")
else:
    st.success("All resumes loaded successfully")

# ---------------- LLM (LM Studio) ----------------
llm = ChatOpenAI(
    model="llama-3.1-8b-instruct",
    temperature=0,
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed"
)

# ---------------- USER QUESTION ----------------
question = st.text_input("Ask a question about the resumes")

if st.button("Get Answer") and question:
    prompt = f"""
You are an HR assistant.

Use the resume data below to answer the question.
If information is not available, say "Not found in resumes".

RESUME DATA:
{all_text}

QUESTION:
{question}
"""

    response = llm.invoke(prompt)
    answer = response.content

    st.subheader("Answer")
    st.write(answer)
