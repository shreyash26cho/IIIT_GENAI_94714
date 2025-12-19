import streamlit as st
import requests
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize LLM (Groq)
llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("🌤️ Weather Explanation App")
st.caption("Enter a city → Get weather → AI explains it")

# User input
city = st.text_input("Enter city name:")

if st.button("Get Weather") and city:
    weather_key = os.getenv("OPEN_WEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        st.error("City not found")
    else:
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        st.subheader("📊 Weather Data")
        st.write("Temperature:", temp, "°C")
        st.write("Humidity:", humidity, "%")
        st.write("Condition:", condition)

        # Ask LLM to explain weather
        prompt = f"""
        The weather in {city} is {condition}.
        Temperature is {temp} degree Celsius and humidity is {humidity} percent.
        Explain this weather in very simple English.
        """

        explanation = llm.invoke(prompt).content

        st.subheader("🧠 Weather Explanation")
        st.write(explanation)
