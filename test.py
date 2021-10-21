import streamlit as st
from auth0_component import login_button
from dotenv import load_dotenv
import os
load_dotenv()

clientId = st.secrets['auth']['clientId']
domain = st.secrets['auth']['domain']

login_button(clientId, domain)


