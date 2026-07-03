# multi-agent-research-assistant
# 🧠 ResearchMind - Multi-Agent AI Research System

ResearchMind is an AI-powered research assistant that uses multiple specialized agents to automatically research any topic and generate a professional report.

## 🚀 Live Demo
🔗 https://multi-agent-research-assistant-qx4ykbyiqxvs4phcqtsrwk.streamlit.app

---

## 📌 Features

- 🔍 Search Agent – Finds relevant information from the web.
- 📖 Reader Agent – Scrapes and extracts useful content.
- ✍️ Writer Agent – Generates a structured research report.
- 📝 Critic Agent – Reviews the report and provides feedback.
- 🎨 Professional Streamlit UI.
- ☁️ Deployed on Streamlit Cloud.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq API (Llama 3.3 70B)
- Tavily Search API
- BeautifulSoup
- Git & GitHub

---

## 🏗️ Project Architecture

```text
User Input
     ↓
Search Agent
     ↓
Reader Agent
     ↓
Writer Agent
     ↓
Critic Agent
     ↓
Final Research Report
```

---

## 📂 Project Structure

```text
multi-agent-research-assistant/
│
├── app.py
├── agents.py
├── tools.py
├── pipeline.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Shrusti1234/multi-agent-research-assistant.git
cd multi-agent-research-assistant
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

#### Windows

```bash
.\.venv\Scripts\Activate.ps1
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:
- Home Page
- Research Pipeline
- Final Research Report

---

## 🌟 Future Improvements

- PDF Report Download
- Export to Word Document
- Research History
- User Authentication
- Citation Management
- Multi-language Support

---

## 👩‍💻 Author

**Shrusti K**

- GitHub: https://github.com/Shrusti1234
- LinkedIn: Add your LinkedIn profile here.

---

## ⭐ If you found this project useful, please give it a star on GitHub!
