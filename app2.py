import streamlit as st

st.title("My age and city app")

age = st.slider("Enter your age", 1 , 100)
city = st.selectbox("Select your city: ", ["Mumbai","Delhi"])

if st.button("Show details"):
    st.write("Your Age:",age)
    st.write("Your City:",city)