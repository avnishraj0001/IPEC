import streamlit as st

st.title("basic calculator app")

num1 = st.number_input("Enter First Number:")
num2 = st.number_input("Enter Second Number:")

operation = st.selectbox("Select Operation:", ["Add","Subtract","Multiply","Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.write(num1 + num2)
    elif operation == "Subtract":
        st.write(num1 - num2)
    elif operation == "Multiply":
        st.write(num1 * num2)
    elif operation == "Divide":
        if num2 != 0:
            st.write(num1 / num2)
        else:
            st.write("cannot divide by zero")