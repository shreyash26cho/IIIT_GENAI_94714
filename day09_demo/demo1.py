

from sentence_transformers import SentenceTransformer
import numpy as np      

def cosine_similarity(a,b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

embed_model = SentenceTransformer('all-MiniLM-L6-v2')
sentences=[
   "l like cricket ",
   "cricket is a great sport",
    "I love to play football",
]
emebeddings = embed_model.encode(sentences)

for embed_vect in emebeddings:
    print("len :", len(embed_vect))


print("similarity between sentence 1 and 2 :", cosine_similarity(emebeddings[0], emebeddings[1]))
print("similarity between sentence 1 and 3 :", cosine_similarity(emebeddings[0], emebeddings[2]))   




