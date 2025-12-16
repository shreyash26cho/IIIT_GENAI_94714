import streamlit as st

with st.form(key="registration_form"):
    st.header("Registration Form")  

    first_name = st.text_input("First Name", key="fname")
    last_name = st.text_input("Last Name", key="lname")
    age = st.slider("Age", 10, 100, 25, 1)
    addr = st.text_area("Address", key="addr")

    submit_button = st.form_submit_button("Submit", type="primary")

if submit_button:
    err_message = ""
    is_error = False

    if not first_name:
        is_error = True
        err_message += "First name cannot be empty.\n"

    if not last_name:
        is_error = True
        err_message += "Last name cannot be empty.\n"

    if not addr:
        is_error = True
        err_message += "Address cannot be empty.\n"

    if is_error:
        st.error(err_message)
    else:
        message = (
            f"Successfully registered:\n"
            f"Name: {first_name} {last_name}\n"
            f"Age: {age}\n"
            f"Address: {addr}"
        )
        st.success(message)
