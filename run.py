# FILE IMPORTS
from set_data import save_application_data
from initialize import initialize_page
from application import application_form
from styling import apply_custom_css

# FILE EXECUTION
from variables import variables_define

# OTHER MODULES
import streamlit as st
import datetime
import json
from pathlib import Path
from streamlit_ace import st_ace


# RUNNING FUNCTION
def execute():
  """Executes the application."""
  initialize_page()
  application_form()
  apply_custom_css()
