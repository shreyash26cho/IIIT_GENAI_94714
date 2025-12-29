import chromadb

db=chromadb.PersistentClient(path="./Resume_base")
content=db.get_or_create_collection("resume")

def add_data(data,metadata,embed,id):
    try:
        content.add(ids=id,embeddings=embed,metadatas=metadata,documents=data)
        print("Data added ...")
        
    except Exception :
        print("failed to Add")


def get_data():
    reult=content.get(include=["embeddings","documents","metadatas"])
    print(reult["embeddings"])
    print("__"*40)
    print(reult["metadatas"])


def delete_data(id):
    try:
        content.delete(ids=[id])
        print(f"deleted {id} succesfully")
    except Exception :
        
        print("fail to delete")

def get_ids():
    all_content=content.get(include=[])
    all_ids=all_content["ids"]
    print(all_ids)
    return all_ids
    

def update_data(data,metadata,embed,id):
    delete_data(id)
    add_data(metadata=metadata,data=data,embed=embed,id=id)


def get_data_for_Embed_query(Equery):
    result=content.query(query_embeddings=Equery,n_results=3,)
    # if result["documents"] != None and result["metadatas"]:
    #     # for data , metadata in zip(result["documents"],result["metadatas"]): 
    #     #     print("Data -->",data)
    #     #     print("Meta data -->",metadata)
    return result
    # else:
    #     print("No data found..")
    #     return None



if __name__=="__main__":
    # path=r"C:\Users\Aarth Shah\OneDrive\Desktop\Sunbeam\IIT_GenAI_94756\Assignment_11\resume\resume-002.pdf"
    # get_data()
    # delete_data('resume-011<built-in method today of type object at 0x00007FFD8D3D0F40>')
    get_ids()



