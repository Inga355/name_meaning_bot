# 🧾 Name Meaning Bot

A simple Python CLI chatbot that asks for a first name and returns a concise meaning, likely origin, and common variants.  
Powered by the OpenAI API.

---

## 🚀 Features
- 🔍 Quick etymology lookup for first names  
- 🎨 Clean CLI interface  
- 🛡️ Basic input validation (letters, spaces, apostrophes, hyphens)  
- 🔁 Simple retry logic for rate limits or API hiccups  
- ⚡ Uses `gpt-4o-mini` for fast and affordable responses  

---

## 📦 Requirements

- Python 3.9+  
- [OpenAI Python SDK](https://pypi.org/project/openai/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Install dependencies:
```bash
pip install -r requirements.txt

---

## 🔑 Setup

1. Create a .env file in the project folder:
    OPENAI_API_KEY=sk-yourapikey

2. (Optional) Use a virtual environment:
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows


---

## ▶️ Run the Bot

- Type a first name → get meaning and origin
- Type exit to quit

### Example:

👋 Hi! Tell me your first name and I'll share its meaning & likely origin.
Type 'exit' to quit.

First name: Alexander

Meaning: Defender of men.
Origin: Greek (Alexandros).
Variants: Alex, Aleksandr, Alejandro

---

## 🛠️ Project Structure

app.py                # Main script
requirements.txt      # Dependencies
.env                  # API key (not committed)

---

## 💡 Ideas to Extend

- Web API with Flask (/name?first=...)
- Multi-language responses
- Caching for popular names
- Structured JSON output for apps

---

## 📜 License

Use freely for learning and experimentation.
