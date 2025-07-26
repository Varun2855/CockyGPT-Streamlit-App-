import streamlit as st

st.set_page_config(page_title="Test App")

st.title("🚀 Streamlit is Working!")

name = st.text_input("What's your name?")

if name:
    st.success(f"Hello, {name}!")