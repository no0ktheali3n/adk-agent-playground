# ADK Agent Playground  
### Version v0.1.1  
A local development environment for experimenting with Google’s Agent Development Kit (ADK), building agents, testing tools, and running the ADK Web UI locally.

This repository evolves from a **single-agent prototype** (v0.1.0) into a **proper ADK project** (v0.1.1) capable of supporting the official ADK web interface and future multi-agent expansion.

---

## 📌 Project Overview

This project contains:

- A working ADK **root agent** using **Gemini 2.5 Flash-Lite**  
- A functioning **Google Search tool**  
- Retry logic using **google-genai HttpRetryOptions**  
- A local Python runner using **InMemoryRunner**  
- A fully ADK-configured agent package (`sample_agent`) that loads correctly in the ADK Web UI  
- Support for environment variables via `.env`  
- Async entrypoint (`main.py`) for local testing  
- Clean directory structure compatible with future multi-agent expansion

---

## 📁 Repository Structure

~~~
adk-agent-playground/
│
├── main.py                     # Local async runner for quick testing
├── agent_config.py             # v0.1.0 agent definition (standalone)
├── sample_agent/               # v0.1.1 ADK-generated agent package
│   ├── agent.py                # ADK-compliant root_agent
│   ├── __init__.py             # Required for package discovery
│   └── .env                    # GOOGLE_API_KEY and backend config
│
├── .gitignore
└── README.md
~~~

---

# 🚀 Version History

## **v0.1.1 — ADK Web UI Integration & Package Structure**
This release introduces a fully compatible ADK agent package, enabling the project to work with the official ADK Web Interface.

### ✅ New Features
- Added `sample_agent/` generated via:
  ~~~
  adk create sample-agent --model gemini-2.5-flash-lite
  ~~~
- Renamed folder from `sample-agent` ➝ `sample_agent` to satisfy Python import rules
- Confirmed ADK discovery and loading inside the Dev UI (`adk web`)
- Isolated agent logic into `sample_agent/agent.py` for ADK-native development
- `.env` inside the package now controls:
  - `GOOGLE_API_KEY`
  - `GOOGLE_GENAI_USE_VERTEXAI`
- Project now supports both **CLI agent interaction** and **browser-based UI**

### ▶️ Running the ADK Web UI

From the project root (`adk-agent-playground/`):

~~~
uv run adk web --port 8000
~~~

Open:

~~~
http://localhost:8000
~~~

You should now see **sample_agent** in the "Select an agent" dropdown.

---

## **v0.1.0 — Initial Local Agent Runner (Standalone)**
The foundational release. Introduces the very first working local agent using Google ADK.

### Features
- Uses **Gemini 2.5 Flash-Lite**
- Configured with the **Google Search tool**
- Includes retry configuration:
  - Up to 5 attempts  
  - Exponential backoff  
  - HTTP retry codes 429/500/503/504  
- Uses `.env` for API key management
- Allows local testing via async runner

### ▶️ Running the Single-Agent Test

From project root:

~~~
uv run main.py
~~~

Produces a chat-like transcript showing:

- User query  
- Model response  
- Search grounding metadata  
- Retry behavior (if triggered)

This version served as the prototype before introducing the full ADK Web UI structure.

---

# ⚙️ Setup Instructions

## 1. Install Dependencies

~~~
uv add google-adk google-genai python-dotenv
~~~

Or via pip:

~~~
pip install google-adk google-genai python-dotenv
~~~

---

## 2. Configure API Key

Add to `.env` (root or inside `sample_agent/.env` depending on which runner you use):

~~~
GOOGLE_API_KEY=your_key_here
GOOGLE_GENAI_USE_VERTEXAI=0
~~~

---

## 3. Running Agents

### **Local Runner (v0.1.0)**

~~~
uv run main.py
~~~

### **ADK Web Interface (v0.1.1)**

Run from the project root:

~~~
uv run adk web --port 8000
~~~

Visit:

~~~
http://localhost:8000
~~~

---

# 🛠 Future Roadmap

This repo is intended to grow into a full agent engineering sandbox. Planned next steps:

- **v0.2.x — Multi-agent support**
  - Add `/agents/` directory
  - Enable agent switching inside the web UI

- **v0.3.x — Custom Tools**
  - File operations
  - Local document retrieval
  - External REST API wrapper tool

- **v0.4.x — ADK Pipeline Experiments**
  - Tool chaining
  - Function calling
  - Memory + stateful agents

- **v0.5.x — Example Agent Suites**
  - Research agent  
  - Summarization agent  
  - Market data agent  
  - Web automation agent (Playwright)  

This repository will form the foundation of a much larger multi-agent development framework under AIien Industries.

---

# 📜 License

MIT License (default, unless changed later).

---

# 💬 Contact

Created and maintained by Tim (“Nook”)  
AIien Industries — AI Automation • Agent Systems • Tooling  

Feel free to open issues or PRs as the project grows.
