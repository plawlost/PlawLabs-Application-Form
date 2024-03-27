# FILE IMPORTS
from set_data import save_application_data
from initialize import initialize_page
from application import application_form
from styling import apply_custom_cs
from variables import variables_define

# OTHER MODULES
import streamlit as st
import datetime
import json
from pathlib import Path
from streamlit_ace import st_ace

# LAST EDITS \\ CHANGE THIS IF YOU SEE
def deletethis():
  """Delete this function."""
  if st.session_state.page_number > 1 and st.session_state.page_number < 15:
    if st.button('Previous Section'):
      st.session_state.page_number -= 1
    if st.button('Next Section'):
      st.session_state.page_number += 1
  
 # RUNNING FUNCTION
 def execute():
     initialize_page()
     application_form()
     apply_custom_css()
     deletethis()