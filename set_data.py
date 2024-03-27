import streamlit as st
import datetime
import json
from pathlib import Path
from streamlit_ace import st_ace

# SAVE APPLICATION INTO JSON DATA
def save_application_data(data, filename_prefix="application_data"):
  """Save application data to a unique file in JSON format."""
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  filename = f"{APPLICATIONS_DIR}/{filename_prefix}_{timestamp}.json"
  with open(filename, "w") as file:
    json.dump(data, file, indent=4)