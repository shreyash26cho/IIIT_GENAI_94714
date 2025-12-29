import streamlit as st
import chromadb
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")


client = chromadb.PersistentClient(path="./chroma-db")
collection = client.get_or_create_collection(name="resume_collection")
resume_files = [
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-001.pdf",
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-002.pdf",
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-003.pdf",
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-004.pdf"z
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-005.pdf"z
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-006.pdf"z
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-007.pdf"z
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-008.pdf"z
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-009.pdf"z
    r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-010.pdf"z




]

def add_resumes(resume_id:str,pdf_path:str):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    full_text=""
    full_text +=page.page_content+"\n"
    embedding = embedding_model.embed_documents([full_text])[0]
    collection.add(
        ids=[resume_id],
        embeddings=[embedding],
        documents=[full_text],
        metadatas=[{
             "resume_id": resume_id,
             "resume_name": os.path.basename(pdf_path),
            "page":len(docs)


        }]

    )
def delete_resume(resume_id):
   collection.delete(ids=[resume_id])

def update_resume(resume_id,new_pdf_path):
    delete resume(resume_id)
    add_resumes(resume_id,new_pdf_path)

def get_all_ewsumes():
    result collection.get(include=["metadatas"])["metadatas"]


st.set    