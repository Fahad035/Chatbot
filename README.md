# 🤖 Gemini Neon Q&A Chatbot

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

A high-performance Q&A Chatbot built with **Streamlit** and **Google Gemini 2.5 API**. This application features a custom **Neon Dark UI**, real-time response generation, and advanced dashboard controls.

---

## ✨ Key Features

* **⚡ Cyber-Neon Interface:** Custom CSS-injected UI with glowing borders and futuristic aesthetics.
* **🧠 Advanced AI Engine:** Utilizes `gemini-2.5-flash-lite` for lightning-fast, high-quota processing.
* **⚙️ Dynamic Control Panel:** Adjust AI creativity (Temperature) and switch models on the fly via the sidebar.
* **💾 One-Click Export:** Download your AI-generated insights as `.txt` files instantly.
* **🛡️ Rate-Limit Protection:** Built-in error handling for `429 Resource Exhausted` errors.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI SDK:** [Google GenAI Python SDK (2026 Edition)](https://pypi.org/project/google-genai/)
* **Styling:** Custom CSS & Markdown
* **Environment:** Python 3.10+

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/Fahad035/Chatbot.git](https://github.com/Fahad035/Chatbot.git)
cd Chatbot
### 2. Install Dependencies
```
pip install -r requirements.txt
### 3. Configure API Key
Create a .env file in the root directory:
GOOGLE_API_KEY=your_gemini_api_key_here
### 4. Launch the App
streamlit run app.py

---

## 📂 Project Structure
```Plaintext
Chatbot/
├── .streamlit/
│   └── config.toml         # Custom theme settings
├── app.py                  # Main application & Neon UI
├── requirements.txt        # Project dependencies
├── .env                    # Secret API keys (Keep private!)
└── README.md               # Documentation

