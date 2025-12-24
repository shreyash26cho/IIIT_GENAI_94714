import chromadb


db = chromadb.PersistentClient(path="./knowledge_base")

collection = db.get_or_create_collection(name="resumes")

collection.add(
    ids=["resume_001"],
    embeddings=[[0.12, -0.45, 0.33]],   
    documents=["This is a sample resume text"],
    metadatas=[{
        "source": "resume_001.pdf",
        "page_count": 2
    }]
)

print("✅ Data added successfully")
print("Total records:", collection.count())
