import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("4893805586e199fdf05ac6ae16e5d413")
if 'login' not in st.session_state:
    st.session_state.login = False



if not st.session_state.login:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == password:
        st.session_state.login = True
    else:
        st.error("Invalid login")

else:
    city = st.text_input("Enter City")

if st.button("Get Weather"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
