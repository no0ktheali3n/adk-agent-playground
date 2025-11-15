# ADK Agent Playground  
![Version](https://img.shields.io/github/v/tag/no0ktheali3n/adk-agent-playground?label=Version&color=blue&style=flat-square)

A development environment for building and testing agents using Google’s **Model-Agnostic Agent Development Kit (ADK)**.  
Designed to evolve from a **single-agent prototype (v0.1.x)** into a **multi-agent orchestration system (v0.2.x)** and eventually into a full **AIien Industries Agent Suite**.

This repo also mirrors the structure and goals of the **Kaggle 5-Day Agent Builder Challenge**, adapted locally, with each version adding capabilities that align with Day 1 → Day 5 of the agent curriculum.

---

# 📌 Project Overview

This playground supports:

- Single-agent and multi-agent ADK workflows  
- Tool-augmented reasoning (Google Search & future custom tools)  
- Gemini 2.5 Flash-Lite integration  
- Multi-agent orchestration patterns  
- ADK Web UI debugging  
- Centralized environment via **uv**  
- Modular, scalable folder structure  
- Versioned roadmap aligned with the 5-Day Agents Intensive  

---

# 📁 Repository Structure (Updated as of v0.2.0)

~~~
adk-agent-playground/                <-- Git repo root + UV environment root
│
├── .venv/                           <-- Single unified environment (uv-managed)
├── pyproject.toml                   <-- Dependencies and tool config
├── README.md                        <-- Project documentation
│
├── main.py                          <-- Optional top-level runner (unused for now)
│
├── adk_agent_multi/                 <-- v0.2.x multi-agent system
│   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── research_agent.py
│   │   └── summarizer_agent.py
│   ├── main.py                      <-- dev runner (requires python -m)
│   ├── agent.py                     <-- root coordinator agent
│   ├── __init__.py                  <-- package marker (required)
│   └── .env
│
├── adk_agent_single/                <-- v0.1.x single-agent baseline
│   ├── main.py
│   ├── agent.py
│   ├── __init__.py
│   └── .env
│
└── sample_agent/                    <-- v0.1.1 ADK-generated agent
    ├── agent.py
    ├── __init__.py
    └── .env
~~~

### Why this structure?

- ADK Web UI auto-detects agents by scanning subfolders containing `agent.py`
- Python requires underscores, not hyphens, for importable modules
- Single shared `.venv` prevents environment fragmentation
- Modular folder structure supports multi-agent orchestration
- Future-proofed for scaling to AIien Industries’ tool suite

---

# 🚀 Version History

## 🔥 v0.2.0 — Multi-Agent System (Research → Summarize → Respond)

This version implements a **three-agent architecture**, passing data amongst 3 agents for research, summarization, and orchestration.

### Agents Included

#### 1. `ResearchAgent`  
- Uses Google Search  
- Returns 2–3 factual findings  
- Output: `research_findings`  

#### 2. `SummarizerAgent`  
- Takes `{research_findings}`  
- Produces 3–5 key bullet points  
- Output: `final_summary`  

#### 3. `ResearchCoordinator` (root agent)  
- Calls ResearchAgent  
- Passes results to SummarizerAgent  
- Produces a refined final answer  
- Registers both sub-agents via `AgentTool`

This is your first complete **coordinated agent workflow**.

---

# ▶️ Running the Multi-Agent System

### **Preferred (module execution)**  
Python requires package context for relative imports.

~~~
uv run python -m adk_agent_multi.main
~~~

### ADK CLI (interactive session)

~~~
uv run adk run adk_agent_multi
~~~

### ADK Web UI

~~~
uv run adk web --port 8000
~~~

Then open:

~~~
http://localhost:8000
~~~


Agents visible in the UI:
- `sample_agent`
- `adk_agent_single`
- `adk_agent_multi`

---

## v0.1.1 — ADK-Compliant Structure + Web UI Integration

### Added
- `sample_agent/` created via:
  ~~~
  adk create sample-agent --model gemini-2.5-flash-lite
  ~~~
- All agent folders updated with `__init__.py` (UI requirement)
- Unified uv environment at project root
- Fixes for folder naming, import rules, and Web UI detection

---

## v0.1.0 — Single-Agent Prototype

### Features
- Standalone Gemini 2.5 Flash-Lite agent
- Google Search tool integration
- Retry logic via `HttpRetryOptions`
- Local `.env` loading
- Async runner (`InMemoryRunner`)

Run via:

~~~
uv run adk_agent_single/main.py
~~~

---

# ⚙ Prerequisites: UV Environment

This project uses **uv** as the package/environment manager.  
All instructions below assume you already have **uv installed locally**.

If you do *not* have uv installed, you can install it in seconds:

### 📥 Install UV (Recommended)
~~~
curl -LsSf https://astral.sh/uv/install.sh | sh
~~~

### 📥 Install UV (Windows PowerShell)
~~~
iwr https://astral.sh/uv/install.ps1 -useb | iex
~~~

### Verify installation
~~~
uv --version
~~~

UV replaces both `pip` and `venv`, offering:
- isolated virtual environments  
- ultra-fast dependency installs  
- Python toolchain management  
- seamless script execution (`uv run ...`)  

Once UV is installed, you can run any agent or development command in this repo exactly as shown.

---

# ⚙ Setup

## This project assumes you have UV installed locally and have already run uv

### Install dependencies
~~~
uv add google-adk google-genai python-dotenv
~~~

### Configure API keys  
Each agent folder contains its own `.env`:

~~~
GOOGLE_API_KEY=your_key_here
GOOGLE_GENAI_USE_VERTEXAI=0
~~~

---

# 🧭 Development Roadmap  
*(Aligned with Kaggle 5-Day Agents Bootcamp adapted for local python development environment)*

## ✔ **v0.1.x — Day 1: Prompt → Action**
- Single agent  
- Tool invocation  
- Local runner  
- ADK UI integration  

## ✔ **v0.2.x — Day 3: Agent Architectures**
- Multi-agent orchestration  
- Research + Summarizer + Coordinator  
- Tool-to-tool data passing  

## 🔜 **v0.3.x — Day 2: Custom Tools & Enhanced Capabilities**
- Add custom tools:
  - Web scraper  
  - Weather API  
  - Market/finance data fetcher  
- Formal tool registry shared across agents  

## 🔜 **v0.4.x — Day 4: Observability & Evaluation**
- Structured logs  
- Latency/throughput metrics  
- Tool-call analytics  
- Error trace visualization  
- Evaluation prompts & regression tests  

## 🔜 **v0.5.x — Day 5: Deployment & Scaling**
- Export agents as services  
- Endpoint-based orchestrator  
- Discord/Slack/Lambda integration  
- Agent2Agent communication patterns  

---

# 🛰 Future: AIien Industries Agent Suite  
A unified framework of production agents:

### Potential Components
- **Research Agent** (v0.2 foundation)  
- **Summarizer Agent**  
- **Financial/Market Data Agent**  
- **Automation Agent (Posting/Scheduling/Monitoring)**  
- **Document RAG Agent**  
- **DevOps / CI/CD Automation Agent**  

These form the basis of a full **AIien Industries automation ecosystem**.

---

# 👤 Maintainer  
**T. ("Nook")**  
Founder — **AIien Industries**  
Applied Intelligence • Agent Systems • Automation Engineering

Feel free to open issues, PRs, or requests as the agent suite expands.