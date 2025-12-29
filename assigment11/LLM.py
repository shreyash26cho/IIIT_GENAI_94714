from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent
import os
from dotenv import load_dotenv
from chroma import *
from embedding import *

load_dotenv()

model=init_chat_model(
    model="moonshotai/kimi-k2-instruct-0905",
    api_key= os.getenv('GROQ_API_key'),
    base_url="https://api.groq.com/openai/v1",
    model_provider='openai'
)

@tool
def update_file(ids,path):
  """
  Updates an existing file in the Chroma database. 
    
    CRITICAL USAGE RULES:
    1. ONLY use this tool when the user explicitly requests to UPDATE, CHANGE, or MODIFY a file.
    2. DO NOT use this tool for searching, listing, or retrieving data. It does not return file content.
    3. If the user asks to "find", "search", or "get" resumes, this tool is NOT applicable.

    Args:
        id (str): The primary key/ID of the file to update (e.g., 'resume-004'). 
                  NOTE: 'Experience' or generic terms are NOT valid IDs.
        path (str): The absolute system path of the new file. Must use double backslashes (e.g., C:\\Users\\Name\\Desktop\\file.pdf).
    """
  print("tool update_file called ")
  update_pdf(ids,path)


agent=create_agent(model=model,
                   tools=[update_file],
                   system_prompt='''
You are an Agentic AI with tool capabilities. Answer the user's question by prioritizing sources in this order:
Provided Context: Use this if relevant. Ignore if not useful.
Tools: Call tools only if the context is missing/irrelevant and the task requires specific external actions. Answer strictly based on tool output.
Internal Knowledge: Use this only if context and tools are not applicable.
Style: Direct answers only. Never explain your decision-making process or state that you are ignoring data. Just provide the solution. in plain text ''')

converation=[]
temp_conversation=[]

def call_model(query,data,metadata):

    data=f"context data = {data} , metadata = {data}, user query={query}"
    temp_conversation=converation.copy()
    temp_conversation.append({"role":"user","content":data})
    output=agent.invoke({"messages":temp_conversation})
    result=output["messages"][-1].content
    print(result)


    converation.append({"role":"user","content":query})
    converation.append({"role":"assistant","content":result})

    return result


if __name__=="__main__":
    call_model("what is Your name","You are a usefull assitant named Ruby","from me.pdf")

