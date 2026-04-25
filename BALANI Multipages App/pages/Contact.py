import streamlit as st

st.title("Contact Me")

name = st.text_input("Your Name")
message = st.text_area("Your Message")

if st.button("Send"):
    st.success("Message sent successfully")