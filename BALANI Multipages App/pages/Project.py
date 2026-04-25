import streamlit as st

st.title("📂 Projects")

projects = {"MINI STREAMLIT APP":"A calculator with multiple functions.",
        "STUDENT MARKETPLACE SYSTEM": "A system for buying and selling within the campus."} 

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)