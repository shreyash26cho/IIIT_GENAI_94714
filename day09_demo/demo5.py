import chromadb
import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# ---------- EMBEDDING MODEL ----------
embed_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------- TEXT SPLITTER ----------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)

# ---------- RAW TEXT ----------
raw_text = """
Kohli has the most Player of the Series and second most Player of the Match awards 
to his name in all three formats combined. He was honoured with the Arjuna Award 
in 2013, the Padma Shri in 2017, and India's highest sporting honour, the Khel Ratna 
Award, in 2018. Time included him on its 100 most influential people in the world 
list in 2018. Kohli has been deemed one of the most commercially viable athletes, 
with estimated earnings of ₹634 crore (US$75 million) in the year 2022.
"""

# ---------- SPLIT INTO CHUNKS ----------
chunks = text_splitter.split_text(raw_text)

# ---------- CREATE EMBEDDINGS ----------
embeddings = embed_model.embed_documents(chunks)

# ---------- CHROMADB ----------
client = chromadb.PersistentClient(path="./chroma-db")
collection = client.get_or_create_collection(name="demo")

ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
metadatas = [{"source": "example.py"} for _ in range(len(chunks))]

collection.add(
    ids=ids,
    embeddings=embeddings,
    documents=chunks,
    metadatas=metadatas
)

print("✅ Documents stored in ChromaDB")

# ---------- QUERY ----------
query = "Who is Virat Kohli?"
query_embedding = embed_model.embed_query(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# ---------- PRINT RESULTS ----------
print("\n🔍 Search Results:\n")

for i, (doc, meta, dist) in enumerate(
    zip(results["documents"][0], results["metadatas"][0], results["distances"][0]),
    start=1
):
    print(f"Result {i}:")
    print(f"Text: {doc}")
    print(f"Metadata: {meta}")
    print(f"Distance: {dist}")
    print("-" * 50)
