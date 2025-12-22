from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain.tools import tool
import os
import requests
import json
import pandas as pd
load_dotenv()


Api_key='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'
print(Api_key)

@tool
def calculater_tool(exprestion):
     '''
    Description this Tool is used to calucalate Mathamatical expreations which contain simple mathamatical operations like + , /,*,- only this much operations it can not ans anything beond this 

    parmeter : this takes in a String of exprestions

    return : this return a ouput of the exprestion in String format 

    error: if it fails to perform the action on  exprestion it returns error    
    '''
     
     return (str(eval(exprestion)))

@tool
def weather_details(city):
     '''
    weather_details  this function is used get the current weather detials of a city that detials are in json format 

    :parameter  city: this parameter takes in  city name as String 

    returns : this gives a json which contain all the the detials about the weather of the given city 

    expection : this gives error when it is not able give a response   

    instrustion : it only gives current detials about weather not past or future  
     '''

     API_key = '4893805586e199fdf05ac6ae16e5d413'
     print(API_key)
     url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
 
     try:
        response=requests.get(url)
        response=response.json()

        return json.dumps(response)
     except Exception as e :
         return ("Erorr to featch data ")
     
@tool   
def get_file_contain(file_path):
    '''
     this tool is use to get file detials when a user gives path of the file note it can only acess .csv files nothing else

     paramether : this use a file path as parameter which is a string 

     responces: this gives a result containing file details  in a string format 

     expection : if it is not able to open file it gives a Error of   file not found  and if not able to find data or featch data it shows error of fail to featch data 

     instraction : the file path must have two backslashes together not single backslashe the path must be like this(eg. C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_4\\Q2\\users.csv not like this  C:/Users/Aarth Shah/OneDrive/Desktop/Sunbeam/IIT_GenAI_94756 Assignment_4/Q2/users.csv ) 
    '''
    try :
        df=pd.read_csv(file_path)
        print(df.head())
        return df
    except Exception :
        return "Error to featch data from the file "

    


@tool
def knowlage_base(topic):
    '''
    knowlage_base this is a fuction which contains information on toipics like How are u , who made u , what is Gen Ai , who is sayama 
    
    :parameter topic: this is parameter takes in topic in str format which heps it to get knowlage on that topic or related 

    result : this returns a string which contains all the info about the topic it needs 

    exception : this gives error is it did not find any topic in this database 

    instruction: the which u will give as input must match the this words with any change to event small or capiatl ( How are U,who made U,Gen Ai,who is Sayama)
    '''

    knowlage = {
        'how are u': "I Am a Ruby A helpfull Assitant which has tools like caluater , open and get file detials or contains , and get latest weather info of a specfic city with a knowlage based for add on info",
        'how are you': "I Am a Ruby A helpfull Assitant which has tools like caluater , open and get file detials or contains , and get latest weather info of a specfic city with a knowlage based for add on info",
        'who made u': "I was desgin and made by Aarth Shah CEO and founder of A S studios and one of the best enginnners on the Earth born on 16 nov 2005  ",
        'gen ai': "Generative AI (GenAI) is a type of artificial intelligence designed to create new content—such as text, images, code, or audio—rather than just analyzing existing data. It works by learning patterns from vast datasets to generate original outputs that resemble human creation based on user prompts."
        
    }
    clean_topic = topic.lower().strip()
    return knowlage.get(clean_topic, f"Sorry, I don't have information in my knowledge base regarding: {topic}")


llm=init_chat_model(
    model="moonshotai/kimi-k2-instruct-0905",
    api_key=Api_key,  
    base_url="https://api.groq.com/openai/v1",
    model_provider="openai"
)

agent=create_agent(model=llm, 
                   tools=[calculater_tool,get_file_contain,knowlage_base,weather_details],
                   system_prompt="You are Ruby, a helpful AI assistant created by Aarth Shah (CEO of A S Studios). For questions about your identity, creator, or specific topics like 'Gen AI' or 'Sayama', you MUST use the 'knowlage_base' tool. Ensure file paths passed to 'get_file_contain' use double backslashes. If a tool returns an error, explain it simply to the user.")

conversation=[]

while True:
    user_input=input("You: ")
    conversation.append({"role":"user","content":user_input})

    respone=agent.invoke({"messages":conversation})
    llm_output= respone["messages"][-1]
    print("AI: ", llm_output.content)

        # print("\n \n all Conversation: ", respone["messages"])
        # print("\n \n orignal response: ", respone)

    conversation= respone["messages"]

    # RESULT= llm.invoke(user_input)
    # print("AI: ", RESULT.content)   

