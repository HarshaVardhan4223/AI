import streamlit as st

# Set page config for better appearance
st.set_page_config(page_title="Simple Streamlit App", layout="centered")

# Title of the application
st.title("Simple Streamlit Application")

# Input text box
name = st.text_input("Enter your name:")

# Button to trigger greeting
if st.button("Greet Me"):
    st.success(f"Hello, {name}! Welcome to Streamlit 🚀")
