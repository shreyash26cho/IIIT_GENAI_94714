import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("4893805586e199fdf05ac6ae16e5d413")

st.title("Login → Weather App")

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------- LOGIN FORM ----------
if not st.session_state.logged_in:
    st.subheader("Login Form")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == password and username != "":
            st.session_state.logged_in = True
        else:
            st.error("Invalid login")

# ---------- WEATHER PAGE ----------
else:
    st.subheader("Weather Information")

    city = st.text_input("Enter City")

    if st.button("Get Weather"):
        if city and API_KEY:
            url = (
                "https://api.openweathermap.org/data/2.5/weather"
                f"?q={city}&appid={API_KEY}&units=metric"
            )
            res = requests.get(url)
            data = res.json()

            if res.status_code == 200:
                st.write("🌡 Temperature:", data["main"]["temp"], "°C")
                st.write("💧 Humidity:", data["main"]["humidity"], "%")
            else:
                st.error("City not found")
        else:
            st.warning("Please enter city name or check API key")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.success("Thanks for visiting 😊")
