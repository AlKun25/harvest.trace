import streamlit as st
import requests
from transaction import SupplyChain, create_transaction

st.set_page_config(page_title="Harvesting", page_icon="🌾")

if "usertype_transactions" in st.session_state:
    st.session_state['usertype_transactions'] = 



# TODO: Show all relevant transactions for this role, with expander to show full transaction timeline
 # Create a form to collect user input

with st.container():
    message = st.text_area("Enter your message:", max_chars=200)
    flagged = st.checkbox("Flag this message")
    if st.button("Submit"):
        

# TODO : Add transaction using button and form.