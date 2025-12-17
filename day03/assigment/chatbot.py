import streamlit as st
import time

# ---------------- TOP RIGHT LOGO ----------------
col1, col2 = st.columns([8, 1])
with col2:
    st.image(
        "https://thumbs.dreamstime.com/b/d-smiling-chatbot-icon-friendly-face-rendering-cheerful-antenna-blue-circle-ideal-ai-tech-branding-vector-410298378.jpg",
        width=50
    )

st.title("🤖 Shin-Ai")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR OPTIONS ----------------
st.sidebar.header("Chat Settings")

show_history = st.sidebar.selectbox(
    "Show Chat History",
    ["Yes", "No"]
)

model = st.sidebar.selectbox(
    "Choose Model",
    ["GPT-4", "LLaMA 3", "Gemini"]
)

research_type = st.sidebar.selectbox(
    "Research Mode",
    ["Simple Research", "Deep Research"]
)


# ---------------- DISPLAY CHAT HISTORY ----------------
if show_history == "Yes":
    for msg in st.session_state.messages:
        st.write(msg)

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Type your message")

if user_input:
    # Save user message
    user_msg = f"🧑 You ({model}): {user_input}"
    st.session_state.messages.append(user_msg)

    # ---------------- BOT REPLY LOGIC ----------------
    def bot_reply():
        msg = user_input.lower().strip()

        if msg in ["hi", "hello", "hey"]:
            reply = "🤖 Shin-Ai: Hi sir, welcome to the chatbot 😊 how can you help me sir?"

        elif msg in ["bye", "exit", "quit"]:
            reply = "🤖 Shin-Ai: Goodbye sir, have a great day 👋"
        else:
            if research_type == "Simple Research":
                reply = f"🤖 Shin-Ai [{model}]: I understood your message: {user_input}"
            else:
                reply = (
                    f"🤖 Shin-Ai [{model}]: I have deeply analyzed your input.\n"
                    f"Here is a detailed response related to: {user_input}"
                )

        for ch in reply:
            yield ch
            time.sleep(0.04)

    # Display bot reply with typing effect
    st.write_stream(bot_reply)

    # ---------------- SAVE BOT MESSAGE ----------------
    msg = user_input.lower().strip()
    if msg in ["hi", "hello", "hey"]:
        bot_msg = "🤖 Shin-Ai: Hi sir, welcome to the chatbot 😊"
    elif msg in ["bye", "exit", "quit"]:
        bot_msg = "🤖 Shin-Ai: Goodbye sir, have a great day 👋"

        
    else:
        if research_type == "Simple Research":
            bot_msg = f"🤖 Shin-Ai [{model}]: I understood your message: {user_input}"
        else:
            bot_msg = (
                f"🤖 Shin-Ai [{model}]: I have deeply analyzed your input. "
                f"Here is a detailed response related to: {user_input}"
            )

    st.session_state.messages.append(bot_msg)
