import streamlit as st
import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# 1. Page Configuration
st.set_page_config(
    page_title="Gemini Pro Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for a sleek look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    [data-testid="stSidebar"] {
        width: 250px !important; 
        padding-top: 0rem !important; 
        background-color: #f1f1f1 !important; 
    }
    [data-testid="stSidebarContent"] {
        padding-top: 0rem !important;   
        padding-left: 1rem !important;  
        padding-right: 1rem !important; 
    }     
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    .response-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #262730;
        border-left: 5px solid #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Load Environment & Client
load_dotenv()
genai_api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=genai_api_key)

# 4. Sidebar - Control Center
with st.sidebar:
    st.title("⚙️ Settings")
    selected_model = st.selectbox(
        "Model Version",
        ["gemini-2.5-flash-lite", "gemini-2.0-flash"],
        help="Lite is faster and has higher limits."
    )
    temperature = st.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)
    st.divider()
    st.info("Status: Connected to Google AI Cluster")

# 5. Main UI Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🚀 Gemini AI Dashboard")
    st.caption("Next-Gen Generative AI Interface")

with col2:
    if st.button("🧹 Clear Chat"):
        st.rerun()

# 6. Chat Interface
st.subheader("Interactive Query")
with st.container():
    with st.form(key='modern_chat'):
        user_input = st.text_area("Enter your prompt here...", placeholder="e.g., Explain Quantum Computing in 2 sentences")
        submit_button = st.form_submit_button(label='Generate Insight')

# 7. Response Logic
if submit_button:
    if user_input:
        with st.spinner("🧠 Processing at the edge..."):
            try:
                # Slight buffer to prevent 429 errors
                time.sleep(0.5)
                
                response = client.models.generate_content(
                    model=selected_model,
                    config={
                        'temperature': temperature,
                    },
                    contents=user_input
                )
                
                # Output Section
                st.success("Analysis Complete")
                st.markdown('<div class="response-container">', unsafe_allow_html=True)
                st.markdown(f"### ✨ Insight\n{response.text}")
                st.markdown('</div>', unsafe_allow_html=True)
                
            except errors.ClientError as e:
                if "429" in str(e):
                    st.error("🚨 Rate limit reached. Please wait 15-30 seconds.")
                else:
                    st.error(f"❌ Error: {e}")
    else:
        st.warning("Please provide an input to generate a response.")


# 8. Footer Analytics (Fake stats for Dashboard look)
st.divider()
foot_col1, foot_col2, foot_col3 = st.columns(3)
foot_col1.metric("Latency", "240ms", "-10ms")
foot_col2.metric("Tokens/sec", "850", "12%")
foot_col3.metric("Model Status", "Healthy")
