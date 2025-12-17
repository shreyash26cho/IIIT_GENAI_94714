import streamlit as st
import pandas as pd
from datetime import datetime

# ---------- FILES ----------
USERS_FILE = "books_hdr.csv"
FILES_FILE = "userfiles.csv"

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.userid = None
    st.session_state.page = "Login"   # FIRST PAGE

# ---------- LOAD CSV ----------
def load_users():
    return pd.read_csv(USERS_FILE)

def load_files():
    return pd.read_csv(FILES_FILE)

# ---------- SAVE CSV ----------
def save_users(df):
    df.to_csv(USERS_FILE, index=False)

def save_files(df):
    df.to_csv(FILES_FILE, index=False)

# ---------- SIDEBAR ----------
st.sidebar.title("Menu")

if not st.session_state.logged_in:
    menu = st.sidebar.radio(
        "Select",
        ["Login", "Register"],
        index=0
    )
else:
    menu = st.sidebar.radio(
        "Select",
        ["Home", "Weather", "Explore CSV", "See History", "Logout"]
    )

# ---------- LOGIN ----------
if menu == "Login":
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()
        user = users[
            (users["username"] == username) &
            (users["password"] == password)
        ]

        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.userid = int(user.iloc[0]["userid"])
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid login")

# ---------- REGISTER ----------
elif menu == "Register":
    st.title("Register Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        users = load_users()

        if username in users["username"].values:
            st.error("User already exists")
        else:
            userid = len(users) + 1
            users.loc[len(users)] = [userid, username, password]
            save_users(users)
            st.success("Registration successful")

# ---------- HOME ----------
elif menu == "Home":
    st.title("Home Page")

    st.write("""
    🌟 Welcome to the Dashboard  
    This application allows you to:
    - Upload CSV files  
    - View upload history  
    - Explore data easily  
    - Check weather information  
    """)

# ---------- WEATHER ----------
elif menu == "Weather":
    st.title("Weather Page")

    city = st.text_input("Enter city name")

    if city:
        st.info(f"Weather feature demo for **{city}**")
        st.write("🌤 Temperature: 30°C")
        st.write("💧 Humidity: 60%")
        st.write("🌬 Wind Speed: 10 km/h")

# ---------- EXPLORE CSV ----------
elif menu == "Explore CSV":
    st.title("Upload CSV")

    file = st.file_uploader("Upload CSV file", type="csv")

    if file:
        df = pd.read_csv(file)
        st.dataframe(df)

        files = load_files()
        files.loc[len(files)] = [
            st.session_state.userid,
            file.name,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ]
        save_files(files)

        st.success("File uploaded and history saved")

# ---------- SEE HISTORY ----------
elif menu == "See History":
    st.title("Upload History")

    files = load_files()
    user_files = files[files["userid"] == st.session_state.userid]

    if user_files.empty:
        st.info("No history found")
    else:
        st.dataframe(user_files)

# ---------- LOGOUT ----------
elif menu == "Logout":
    st.session_state.logged_in = False
    st.session_state.userid = None
    st.session_state.page = "Login"
    st.success("Logged out")
    st.rerun()
