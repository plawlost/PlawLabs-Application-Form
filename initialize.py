import streamlit as st
import datetime
import json
from pathlib import Path
from streamlit_ace import st_ace

# INITIALIZE APP
def initialize_page():
    """Set up page configuration and initialize session state variables."""
    st.set_page_config(page_title="PlawLabs Application Portal", layout="wide")
    if 'page_number' not in st.session_state:
      st.session_state.page_number = 1

    if "application_data" not in st.session_state:
      st.session_state.application_data = {}
      # Initialize session state variables for the application data
      st.image("plawlabs_icon_v2.png", width=100) # logo