import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to harvest.trace! 👋")

st.sidebar.success("Select a demo above.")

# TODO : Load all page specific transactions in state variables by their names