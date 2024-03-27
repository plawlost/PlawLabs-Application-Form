import streamlit as st
import datetime
import json
from pathlib import Path
from streamlit_ace import st_ace

# CSS STYLING
def apply_custom_css():
    """Apply custom CSS to the Streamlit app."""
    custom_css = """
      <style>
       .main {
        background-color: #0E1117; /* Deep, dark background */
        font-family: 'Roboto', sans-serif; /* Sleek, modern font */
       }
      
       ::placeholder {
        color: #A9B3C1; 
       }
      
       /* Input fields */
       .stTextInput > div > div > input, 
       .stSelectbox > div > div > select, 
       .stDateInput > div > div > input,
       .stTextArea > textarea {
        color: #F0F2F6; 
        background-color: #1F2937; 
        border: 1px solid #334155; 
       }
      
       /* Container Boxes */
       .st-bb, .st-bj, .st-cj, .st-cx, .st-ck {
        background-color: #18202C; /* Slightly lighter container shade */
        color: #ffffff;
        border: 1px solid #25303E; /* Darker border */
       }
      
       /* Buttons (Let's add some magic) */
       .st-bs, .st-bj, .st-cj, .st-cx, .st-ck { /* Target all button-like elements*/
        background: linear-gradient(145deg, #232a34, #18202c); /* Subtle gradient */
        color: #F0F2F6;
        border: none; /* Remove default border */
        box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.4); /* Subtle shadow */
        transition: all 0.2s ease-in-out; /* Smooth transition */
       }
      
       .st-bs:hover, .st-bj:hover, .st-cj:hover, .st-cx:hover, .st-ck:hover {
        background: #FFC83D; /* Your vibrant orangish-yellow on hover */ 
        color: #11151C; /* Dark contrast text */
        box-shadow: 3px 4px 8px rgba(0, 0, 0, 0.6); /* More pronounced shadow */
       }
      """
    st.markdown(custom_css, unsafe_allow_html=True)