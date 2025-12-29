from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

resume_files=[
r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-001.pdf",
r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-002.pdf",
r"C:\\Users\\shrey\\Desktop\\GenAI\\IIIT_GENAI_94714\\day09_demo\\resume\\resume-003.pdf"
]
all_docs=[]
for resume_path in resume_files:
    loader=PyPDFLoader(resume_path)
    docs=loader.load()
for page in docs:
    page.metadata["resume_name"]=resume_path.split("\\")[-1]
all_docs.extend(docs)




for page in all_docs:
    print("resume:",page.metadata["resume_name"])
    print(page.page_content)
    print(page.metadata)
    print("-"*50)

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(all_docs)

for chunk in chunks:
    print("resume:",chunk.metadata["resume_name"])
    print(chunk.page_content)
    print("="*50)
    


