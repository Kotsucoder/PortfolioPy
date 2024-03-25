import streamlit as st
from send_email import send_email

st.header("Contact Me")


with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"Subject: Message from {user_email} on Streamlit\n{raw_message}"
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")