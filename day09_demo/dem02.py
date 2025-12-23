from langchain_openai import OpenAIEmbeddings
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

embed_model = OpenAIEmbeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy-token",
    check_embedding_ctx_length=False
)

sentences = [
    "I like cricket ",
    "cricket is a great sport",
    "I love to play football",
]

embeddings = embed_model.embed_documents(sentences)

for emb in embeddings:
    print("len :", len(emb))

print(
    "similarity between sentence 1 and 2 :",
    cosine_similarity(embeddings[0], embeddings[1])
)

print(
    "similarity between sentence 1 and 3 :",
    cosine_similarity(embeddings[0], embeddings[2])
)
