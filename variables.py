import streamlit as st
import datetime
import json
from pathlib import Path
from streamlit_ace import st_ace

# GLOBAL VARIABLES
def variables_define():
  """Set global variables."""
  APPLICATIONS_DIR = "applications_data"
  Path(APPLICATIONS_DIR).mkdir(parents=True, exist_ok=True)