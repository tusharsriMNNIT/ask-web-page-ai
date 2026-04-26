# Ask Web Page AI

Ask questions about any webpage directly inside Chrome using a local LLM powered by Ollama.

This project combines:

- Chrome Extension (frontend)
- Python Flask backend
- Ollama running locally
- LangChain integration

When visiting any webpage, you can open the extension popup, ask a question, and get answers based on the current page content.

---

# Features

- Ask questions about any webpage
- Uses local LLMs via Ollama
- No cloud API required
- Works with Chrome extension popup UI
- Python backend with Flask

---

# Project Structure

```text
chrome-ollama-extension/
│── backend/
│   ├── app.py
│   ├── requirements.txt
│
│── extension/
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   ├── content.js
```

---

# Prerequisites

Install the following before starting:

- Python 3.10+
- Google Chrome
- Ollama

---

# 1. Install Ollama

Download and install Ollama from:

https://ollama.com/download

After installation, verify:

```bash
ollama --version
```

---

# 2. Pull a Model

Download a local model (recommended: llama3):

```bash
ollama pull llama3
```

You can also use other models:

```bash
ollama pull mistral
ollama pull gemma
ollama pull qwen
```

To list installed models:

```bash
ollama list
```

To start Ollama server:

```bash
ollama serve
```

---

# 3. Create Python Virtual Environment

Go to backend folder:

```bash
cd backend
```

Create virtual environment:

## macOS / Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

## Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

---

# 4. Install Requirements

Create `requirements.txt`:

```text
flask
flask-cors
langchain
langchain-community
langchain-ollama
beautifulsoup4
requests
```

Install packages:

```bash
pip install -r requirements.txt
```

---

# 5. Run Backend Server

Inside backend folder:

```bash
python app.py
```

Expected output:

```text
Running on http://127.0.0.1:5000
```

Keep this terminal running.

---

# 6. Load Chrome Extension

Open Google Chrome and go to:

```text
chrome://extensions
```

Enable:

```text
Developer Mode
```

Click:

```text
Load unpacked
```

Select the `extension/` folder from this project.

---

# 7. How to Use

1. Open any webpage in Chrome
2. Click the extension icon
3. Type a question such as:

- Summarize this page
- What product is this?
- What are the key features?
- Explain this page simply

4. Get answers from your local Ollama model

---

# Example Questions

- Summarize this article
- What is this product about?
- Extract important points
- Compare features mentioned here
- Explain this topic to a beginner

---

# Troubleshooting

## Ollama not found

Make sure Ollama is installed:

```bash
ollama --version
```

## Model missing

Pull model again:

```bash
ollama pull llama3
```

## Backend not starting

Install requirements:

```bash
pip install -r requirements.txt
```

## Extension not working

- Reload extension in Chrome
- Make sure Flask server is running on port 5000
- Ensure Ollama is running

---

# Future Improvements

- Sidebar chat UI
- Streaming responses
- Ask selected text
- Multi-turn memory chat
- Better page extraction
- Support multiple models

---

# License

MIT License

---

# Author

Built by Tushar
