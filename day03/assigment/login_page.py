import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ---------- FILES ----------
USERS_FILE = "user.csv"
FILES_FILE = "userfiles.csv"

# ---------- CREATE FILES IF NOT EXIST ----------
if not os.path.exists(USERS_FILE):
    pd.DataFrame(
        columns=["userid", "username", "password"]
    ).to_csv(USERS_FILE, index=False)

if not os.path.exists(FILES_FILE):
    pd.DataFrame(
        columns=["userid", "filename", "upload_time"]
    ).to_csv(FILES_FILE, index=False)

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.userid = None

# ---------- LOAD CSV ----------
def load_users():
    df = pd.read_csv(USERS_FILE)
    df.columns = df.columns.str.strip()
    if not df.empty:
        df["username"] = df["username"].astype(str).str.strip()
        df["password"] = df["password"].astype(str).str.strip()
    return df

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
    menu = st.sidebar.radio("Select", ["Login", "Register"])
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

        username = username.strip()
        password = password.strip()

        if users.empty:
            st.error("No users found. Please register first.")
        else:
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
                st.error("Invalid username or password")

# ---------- REGISTER ----------
elif menu == "Register":
    st.title("Register Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        users = load_users()

        username = username.strip()
        password = password.strip()

        if username == "" or password == "":
            st.error("Username and password required")

        elif not users.empty and username in users["username"].values:
            st.error("User already exists")

        else:
            userid = 1 if users.empty else users["userid"].max() + 1
            users.loc[len(users)] = [userid, username, password]
            save_users(users)
            st.success("Registration successful. You can login now.")

# ---------- HOME ----------
elif menu == "Home":
    st.title("Home Page")
    st.write("""
    🌟 **Welcome to the Dashboard**
    - Upload CSV files  
    - View upload history  
    - Explore CSV data  
    - Weather demo  
    """)

# ---------- WEATHER ----------
elif menu == "Weather":
    st.title("Weather Page")

    city = st.text_input("Enter city name")
    if city:
        st.info(f"Weather demo for **{city}**")
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

        st.success("File uploaded & history saved")

# ---------- SEE HISTORY ----------
elif menu == "See History":
    st.title("Upload History")

    files = load_files()
    user_files = files[files["userid"] == st.session_state.userid]

    if user_files.empty:
        st.info("No upload history found")
    else:
        st.dataframe(user_files)

# ---------- LOGOUT ----------
elif menu == "Logout":
    st.session_state.logged_in = False
    st.session_state.userid = None
    st.success("Logged out successfully")
    st.rerun()
