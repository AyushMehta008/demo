import streamlit as st

st.title("🔐 Login")

# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Login successful! 🎉")
    else:
        st.error("Invalid username or password")

        