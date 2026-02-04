import streamlit as st

st.title("simple input app")

name = st.text_input("Enter your Name:")

if st.button("Submit"):
    st.write("Hello", name)
    