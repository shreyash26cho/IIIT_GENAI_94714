import requests
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv('GROQ_API_KEY')
)

city = input("enter the city: ")
api_key =os.getenv('OPEN_WEATHER_API_KEY')

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

temp = data["main"]["temp"]
weather = data["weather"][0]["description"]

print("temperature:", temp)
print("weather:", weather)

prompt = f"""
The weather in {city} is {weather}.
The temperature is {temp} degree Celsius.
Explain this weather in simple English.
"""

result = llm.invoke(prompt)

print("\nLLM Explanation:")
print(result.content)
