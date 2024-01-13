# https://docs.streamlit.io/get-started/installation/command-line


import os
from dotenv import load_dotenv
import streamlit as st
from gpt_utils import generate_prompt

with open('instruction_mj.txt', 'r') as file:
    text_from_file = file.read().strip()


# Load environment variables
load_dotenv()

# Get API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

# Streamlit page configuration
st.set_page_config(
    page_title="Prompt Improver",  # Set the title of the page
    layout="wide",                # Use the full width of the screen
    initial_sidebar_state="auto", # 'auto' means the sidebar state adapts to the user's interaction (expanded or collapsed)
    menu_items={                  # Additional menu items in the hamburger menu
        'Get Help': 'https://www.example.com/help',
        'Report a bug': "https://www.example.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Title
st.markdown("<h1 style='text-align: center;'>3.5 Prompt Helper</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    .inputbox {
        height: 2000px;  /* or the height you prefer */
        width: 500px;  /* or the width you prefer */
    }
    </style>
    """, unsafe_allow_html=True)

# User input
instruction = st.text_area("Enter your instruction:", text_from_file, height=300)
user_prompt = st.text_area("Enter your prompt:", "a cute girl eating a burger")



# Button to generate improved prompts
if st.button("Generate Improved Prompts"):
    improved_prompt_pika = generate_prompt(user_prompt, instruction)

    # Display editable text blocks
    st.text_area("For Pika:", value=improved_prompt_pika, height=100)
