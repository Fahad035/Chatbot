# Q&A chatbot using streamlit and google's generative ai

from dotenv import load_dotenv
import streamlit as st
import os
import textwrap

import google.generativeai as genai
from IPython.display import display, Markdown

# Load environment variables
load_dotenv()

genai_api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=genai_api_key)
# Function to intract with the gemini generative AI model and get a response

def get_gemini_response(question):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(question)
    return response.text

# Initialize the Streamlit app with a contain page title

st.set_page_config(page_title="Question & Answer bot")

# Display the header for the application

st.header("Gemini Chatbot")

input = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

if submit:
    response=get_gemini_response(input)

    st.subheader("The response is")
    st.write(response)

