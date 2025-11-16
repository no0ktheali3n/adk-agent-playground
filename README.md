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

# 📁 Repository Structure (Updated as of v0.2.1)

~~~
adk-agent-playground/                <-- Git repo root + UV environment root
│
├── .venv/                           <-- Single unified environment (uv-managed)
├── .env                             <-- Environment variables live in root directory
├── pyproject.toml                   <-- Dependencies and tool config
├── README.md                        <-- Project documentation
│
├── main.py                          <-- Optional top-level runner (unused for now)
│
├── adk_agent_multi/                 <-- v0.2.0 multi-agent system
│   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── research_agent.py
│   │   └── summarizer_agent.py
│   ├── __init__.py                  <-- package marker (required)
│   ├── agent.py                     <-- root coordinator agent
│   └── main.py                      <-- local dev runner (requires python -m)
│
├── adk_agent_sequence/              <-- v0.2.1 sequential agent system
│   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── editor_agent.py
│   │   ├── outline_agent.py
│   │   └── writer_agent.py
│   ├── __init__.py                  <-- package marker (required)
│   ├── agent.py                     <-- root coordinator agent
│   └── main.py                      <-- local dev runner (requires python -m)
|
├── adk_agent_single/                <-- v0.1.x single-agent baseline
│   ├── __init__.py                  <-- package marker (required)
│   ├── agent.py                     <-- root coordinator agent
│   └── main.py                      <-- local dev runner (doesn't require -m flag due to no nested sub_agent structure)
│
├── sample_agent/                    <-- v0.1.1 ADK-generated agent
|   ├── __init__.py
└─  └── agent.py
~~~

### Why this structure?

- ADK Web UI auto-detects agents by scanning subfolders containing `agent.py`
- Python requires underscores, not hyphens, for importable modules
- Single shared `.venv` prevents environment fragmentation
- Modular folder structure supports multi-agent orchestration
- Future-proofed for scaling to AIien Industries’ tool suite

---

# 🚀 Version History

## 🔥 v0.2.1 — Sequential Agent Pipeline (Outline → Draft → Edit)

This update extends the v0.2.x multi-agent architecture by introducing a fully structured **SequentialAgent pipeline**, implemented in a new module:

~~~
adk_agent_sequence/
~~~

### ✔ New Capabilities

This version demonstrates a **deterministic, assembly-line workflow**, where each agent executes in strict order and passes its output to the next stage:

1. **OutlineAgent**  
   Creates a structured blog outline with headline + sections.

2. **WriterAgent**  
   Expands the outline into a 200–300 word blog draft.

3. **EditorAgent**  
   Polishes the draft for grammar, flow, clarity, and style.

These three sub-agents are wrapped by a `SequentialAgent` named **BlogPipeline**, ensuring predictable, ordered multi-agent behavior. Each agent automatically receives the previous agent’s output via ADK’s state injection.

### ✔ Example Workflow

~~~
User → OutlineAgent → WriterAgent → EditorAgent → Final Output
~~~

### ✔ Runner

A new local runner is included:

~~~bash
uv run python -m adk_agent_sequence.main
~~~

This script:

- Loads configuration from the **top-level `.env` only**  
- Initializes the BlogPipeline sequential agent  
- Executes a full outline → draft → edit cycle  
- Displays a complete debug trace via `run_debug()`

### ✔ Directory Update

The repository has been simplified so that **only one `.env` file** lives at the repository root (`adk-agent-playground/.env`).  
All nested `.env` files have been removed in this version, as ADK resolves environment variables globally during local execution.

This release completes the **Sequential Agent** workflow and sets the foundation for:

- **v0.2.2 — Parallel Agents**  
- **v0.2.3 — Loop / Iterative Agents**  

which will continue expanding the v0.2.x multi-agent exploration series.


## 🔥 v0.2.0 — Multi-Agent System (Research → Summarize → Respond)

This version implements a **three-agent architecture**, passing data amongst 3 agents for research, summarization, and LLM orchestration.

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

## This project assumes you have UV installed locally and have already run uv init

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
*(Guided by the Kaggle 5-Day Agents Bootcamp adapted to a local python development environment, but versioned according to actual functionality added to this repository.)*

The 5-Day curriculum serves as a **technical progression guide**, not a strict versioning schedule.  
We will increment versions **when meaningful capability changes occur**, even if a single bootcamp day results in multiple internal updates.

---

## ✔ **v0.1.x – Foundations (Day 1: Single Agent)**  
**Bootcamp Themes:**  
• Introduction to agents  
• Agent taxonomy, policies, identity, reliability  
• Build your first agent (Gemini + ADK)  
• Add Google Search as a tool  

**Repository Achievements:**  
- Implemented a working single-agent system  
- Local runner using `InMemoryRunner`  
- Retry logic + `.env` configuration  
- Added ADK Web UI compatibility

This corresponds to the *first half* of Day 1.

---

## ✔ **v0.2.x – Multi-Agent Architectures (Day 1: Multi-Agent)**  
**Bootcamp Themes:**  
• Multi-agent design patterns  
• Specialized roles  
• Agent coordination models  
• Using tools across agents  

**Repository Achievements:**  
- Introduced multi-agent orchestration  
- Added ResearchAgent + SummarizerAgent  
- Root coordinator agent using `AgentTool`  
- Completed a coordinated workflow  

This corresponds to the *second half* of Day 1.

---

## 🔜 **v0.3.x – Agent Tools, MCP, & Long-Running Operations (Day 2)**  
**Bootcamp Themes:**  
• Designing custom tools  
• Best practices for safe tools  
• Model Context Protocol (MCP)  
• Long-running tool calls  
• Human-in-the-loop approval patterns  

**Planned Repository Additions:**  
- Convert Python functions into ADK tools  
- Introduce first MCP-compliant tool(s)  
- Implement a long-running operation example  
- Add human-approval checkpoints for tools  
- Build shared tool registry (usable by any agent)

This may be released as **multiple sub-versions (v0.3.0, v0.3.1, v0.3.2)** depending on complexity.

---

## 🔜 **v0.4.x – Sessions, Memory & Stateful Agents (Day 3)**  
**Bootcamp Themes:**  
• Context engineering  
• Sessions (short-term conversation state)  
• Memory (long-term persistent state)  
• Coherent multi-turn dialogue  

**Planned Repository Additions:**  
- Add session-level working memory  
- Add persistent long-term memory store  
- Build stateful agents with evolving context  
- Memory modules configurable per-agent  
- Optional: shared memory for multi-agent systems  

This release expands the playground from "stateless" to "intelligent + continuous."

---

## 🔜 **v0.5.x – Observability, Logging, Traces & Evaluation (Day 4)**  
**Bootcamp Themes:**  
• Logs = the diary  
• Traces = the narrative  
• Metrics = health and performance  
• Evaluation frameworks (LLM-as-a-judge, HITL)  

**Planned Repository Additions:**  
- Unified structured logging across all agents  
- Execution traces for multi-agent workflows  
- Debug panels for tool-calling behavior  
- Metrics: latency, tokens, decision depth  
- Evaluation harness for scoring agent output  
- Regression testing suite  

This improves reliability, confidence, and reproducibility.

---

## 🔜 **v0.6.x – Prototype → Production (Day 5)**  
**Bootcamp Themes:**  
• Deployment patterns  
• A2A Protocol (Agent-to-Agent communication)  
• Independent multi-agent services  
• Productionization workflows  
• Optional cloud deployment (Vertex Agent Engine)  

**Planned Repository Additions:**  
- Local A2A communication module  
- Standalone agent services (run as microservices)  
- Multi-agent network simulations  
- Deployment-ready folder structure  
- Optional: scripts for cloud deployment  
- Optional: Vertex Agent Engine adaptation  

This phase establishes real scalability and interoperability.

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