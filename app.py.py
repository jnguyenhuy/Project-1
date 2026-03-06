import streamlit as st

st.title("My First Streamlit App")
st.write("Hello! This is my first app.")

name = st.text_input("What's your name?")

if st.button("Say hi"):
    st.success(f"Hi, {name}!")