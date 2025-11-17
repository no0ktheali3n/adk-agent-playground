# ADK Agent Playground  
![Version](https://img.shields.io/github/v/tag/no0ktheali3n/adk-agent-playground?label=Version&color=blue&style=flat-square&cacheSeconds=0)

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

# 📁 Repository Structure (Updated as of v0.2.4)

~~~
adk-agent-playground/                <-- Git repo root + UV environment root
│
├── .venv/                           <-- Single unified environment (uv-managed)
├── .env                             <-- Environment variables live in root directory
├── pyproject.toml                   <-- Dependencies and tool config
├── README.md                        <-- Project documentation
│
├── main.py                          <-- Optional top-level runner (unused for now)
|
├──adk_agent_loop/                   <-- v0.2.3 agent refinement loop system
|   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── critic_agent.py
│   │   ├── initial_writer_agent.py
│   │   └── refiner_agent.py
|   │
|   ├── agent.py                     <-- LoopAgent + Sequential wrapper (StoryRefinementLoop + StoryPipeline)
|   └── main.py                      <-- Local test runner for the loop workflow
|
├── adk_agent_multi/                 <-- v0.2.0 multi-agent system
│   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── research_agent.py
│   │   └── summarizer_agent.py
│   ├── __init__.py                  <-- package marker (required)
│   ├── agent.py                     <-- root coordinator agent
│   └── main.py                      <-- local dev runner (requires python -m)
│
├── adk_agent_parallel/              <-- v0.2.2 concurrent agent system
│   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── aggregator_agent.py
│   │   ├── finance_researcher.py
│   │   ├── health_researcher.py
│   │   └── tech_researcher.py
│   ├── __init__.py                  <-- package marker (required)
│   ├── agent.py                     <-- root coordinator agent, contains ParallelAgent and SequentialAgent
│   └── main.py                      <-- local dev runner (requires python -m)
|
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
|
├──common/
|   ├── __init__.py  # Package marker (kept intentionally minimal)
|   ├── llm.py       # Canonical retry config + shared LLM constructors
|   └── tools.py     # Shared Google Search & future tools
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

# 🧭 Workflow Pattern Summary — Choosing the Right Multi-Agent Architecture

As of v0.2.3–v0.2.4, this project now includes **all three core Day 1 workflow patterns**:

- **Sequential workflows**
- **Parallel workflows**
- **Loop / iterative refinement workflows**

This section summarizes when to use each pattern, what they excel at, and how they differ — serving as a quick reference when designing new agents.

---

## 🔍 Decision Guide: Which Workflow Pattern Should You Use?

                  ┌──────────────────────────────────────────┐
                  │   What kind of workflow do you need?     │
                  └──────────────────────────────────────────┘
                          /       |        |        \
                         /        |        |         \
                        v         v        v          v
               Fixed order   Concurrent   Refinement   Dynamic decisions
               (A → B → C)    tasks        (A ↔ B)     (LLM chooses path)

                  Use           Use          Use              Use
      **SequentialAgent** **ParallelAgent** **LoopAgent**  LLM Orchestrator


---

## 📘 Quick Reference Table

A compact comparison of all available workflow patterns:

| **Pattern**                | **When to Use**                                 | **Example**                         | **Key Feature**                      |
|----------------------------|-------------------------------------------------|-------------------------------------|--------------------------------------|
| **LLM-based (sub_agents)** | Dynamic orchestration needed                    | Research → Summarize                | LLM decides the workflow steps       |
| **Sequential**             | Steps must run in a strict linear order         | Outline → Write → Edit              | Deterministic, predictable pipeline  |
| **Parallel**               | Tasks are independent; speed is important       | Multi-topic research                | True concurrent execution            |
| **Loop**                   | Refinement cycles needed; quality control       | Writer ↔ Critic refinement loop     | Repeated passes until stopping rules |

---

## 🧩 How These Fit Into v0.2.x

Each pattern is represented by its own module:

- `adk_agent_sequence/` → **Sequential pipeline**
- `adk_agent_parallel/` → **Parallel execution team**
- `adk_agent_loop/` → **Loop-based refinement**
- `adk_agent_multi/` → **LLM-orchestrated dynamic multi-agent system**

This gives you a complete working library of reference architectures you can reuse, remix, or extend for future experimental agents.

---

## 🚀 What This Means for Future Development

With these workflows implemented and documented, the project became ready to evolve into:

- Custom toolchains  
- Model Context Protocol (MCP) tools  
- Stateful sessions & memory  
- Long-running operations  
- Cross-agent communication patterns  
- Production-grade pipelines  

This section wrapped up the foundational workflows (v0.2.x) and prepared the repo for the v0.3.x+ developments.

---


# 🚀 Version History

## 🔧 v0.2.4 — Common Module Refactor & Codebase Slimming

This update introduces a major internal cleanup to the multi-agent modules by centralizing shared logic into a new `common/` package.  
The result is a **leaner, more maintainable, and more scalable codebase** that prepares the playground for the upcoming v0.3.x “Custom Tools + MCP” phase.

---

### ✔ What Changed in v0.2.4

Three agent systems now use shared modules instead of repeating boilerplate:

- `adk_agent_sequence/`
- `adk_agent_parallel/`
- `adk_agent_loop/`

These modules now import from:

common/  
│  
├── `llm.py`  ← Shared LLM constructors + retry config  
└── `tools.py`  ← Shared Google Search tool + future custom tools  

All repeated logic — especially the `Gemini` model setup, `HttpRetryOptions`, and tool imports — is consolidated here.

---

### ✔ Purpose of This Refactor

This refactor solves several pain points discovered during development:

#### 1. Eliminates Repetition Across Sub-Agents

Previously, every agent/sub-agent repeated the same imports:

- `Gemini` model definition  
- `retry_config` block  
- `google_search` tool import  
- `types.HttpRetryOptions`  
- ADK boilerplate  

Now these are defined once, in one place.

This cuts roughly **20–30% of repeated code** across the affected modules.

---

#### 2. Makes Future Model Swaps or Expansions Much Easier

Because models now live in `common/llm.py`, you can:

- Add new model constructors (e.g., `gemini_flash`, `gemini_pro`, future variants)  
- Change retry behavior globally in a single file  
- Introduce profile-specific LLMs (e.g., researcher vs editor vs critic)

…all **without editing every agent file**.

---

#### 3. Prepares the Playground for v0.3.x+

The next version series' (v0.3.x+) will introduce:

- Custom tools  
- MCP interoperability  
- Shared registries  
- Long-running operations  
- Early context/memory abstractions  

A centralized `common/` directory is the right architecture for this next stage.

---

### ✔ Modules Updated in This Release

- `adk_agent_sequence/` ← Refactored to use `common.llm` and `common.tools`  
- `adk_agent_parallel/` ← Same refactor applied  
- `adk_agent_loop/` ← Same refactor applied  

Left intentionally unchanged for contrast:

- `adk_agent_multi/` ← Old multi-agent structure kept for comparison  
- `adk_agent_single/` ← Historical single-agent baseline  

This allows developers to clearly **compare the old vs new architecture** while the project evolves.

---

### ✔ Directory Layout (new + relevant parts)

~~~
common/
│
├── __init__.py  # Package marker (kept intentionally minimal)
├── llm.py       # Canonical retry config + shared LLM constructors
└── tools.py     # Shared Google Search & future tools

adk_agent_loop/
adk_agent_parallel/
adk_agent_sequence/
└── sub_agents/  # Reduced boilerplate, cleaner imports
~~~

---

### ✔ Impact Summary

- 🔻 **20–30% reduction in repeated code** across multi-agent modules  
- ✔ **Cleaner sub-agent files**, easier to read and reason about  
- ✔ **Centralized retry logic**, ensuring consistent behavior  
- 🔧 **LLM definitions now hot-swappable** from a single location  
- 🚀 Prepares the repo for **custom tools**, **MCP**, and other Day 2+ features  

This is a foundational cleanup step that strengthens the codebase before we move into more advanced agent capabilities.


## 🌀 v0.2.3 — Loop Workflows: Iterative Refinement with LoopAgent  
This update introduces **iterative multi-agent refinement** using a `LoopAgent`, completing the final pattern from Day 1 of the Agent Builder curriculum.  
Unlike sequential or parallel agents that run once, loop agents enable **feedback cycles**, **quality improvement**, and **conditional termination**.

This version adds a complete **Story Writing + Critique Loop** system where a draft is repeatedly refined until approved by a critic.

---

`adk_agent_loop/`

### ✓ New Capabilities

This module demonstrates a **refinement cycle** powered by a `LoopAgent`, where agents run repeatedly until a stop condition is met or a maximum number of iterations is reached.

The workflow includes:

1. **InitialWriterAgent**  
   Produces the first draft of a short story (100–150 words).  
   - No tools  
   - Output: `current_story`

2. **CriticAgent**  
   Reviews the draft and either:  
   - Returns actionable critique (`critique`)  
   - Or responds with **“APPROVED”** exactly, which signals the loop to stop.  
   - Output: `critique`

3. **exit_loop() → FunctionTool**  
   A Python function wrapped as a callable tool.  
   When invoked, it returns a structured payload the `LoopAgent` recognizes as a termination signal.

4. **RefinerAgent**  
   Reads the critic’s feedback and decides:  
   - If critique == **APPROVED**, call the `exit_loop` tool  
   - Otherwise rewrite the story, updating `current_story` with a refined version  
   - Output: updated `current_story`

These agents are wrapped in:

- **StoryRefinementLoop (LoopAgent)** — runs Critic → Refiner repeatedly  
- **StoryPipeline (SequentialAgent)** — runs InitialWriter once, then runs the refinement loop

---

### ✓ Workflow Summary

User → InitialWriter → (Critic ↔ Refiner Loop) → Final Story

The loop runs up to `max_iterations=2`, preventing infinite cycles while still allowing meaningful refinement.

---

### ✓ Runner

Included test runner:

~~~text
uv run python -m adk_agent_loop.main
~~~

This runner:

- Loads `.env` from the repository root  
- Executes the full **write → critique → refine** loop  
- Prints the detailed `run_debug()` trace for full visibility  
- Produces a finalized short story that has been explicitly approved by the critic

---

### ✓ Purpose of This Version

v0.2.3 completes the trio of Day 1 multi-agent workflow patterns:

- **v0.2.1 — Sequential Workflows**  
- **v0.2.2 — Parallel Workflows**  
- **v0.2.3 — Loop Workflows**

With all three patterns implemented cleanly and modularly, the repo is now fully prepared for the next phase (v0.3.x series), which will introduce:

- Custom tools  
- MCP-based tools  
- Long-running operations  
- Shared tool registries  
- Early context/memory features

---

This version finalizes the foundational architecture for **all core multi-agent control-flow patterns** in the ADK ecosystem within this playground.

## 🔷 v0.2.2 — Parallel Multi-Topic Research System (Concurrent Agents)

This update introduces **parallel agent execution**, enabling multiple independent researchers to run **simultaneously** and dramatically improve throughput compared to sequential pipelines.

This version adds a new project:

`adk_agent_parallel/`

### ✓ New Capabilities

This system demonstrates **concurrent, independent multi-agent workflows**, where multiple specialists run in parallel and their results are combined by an aggregator.

Four agents make up the full workflow:

1. **TechResearcher**
   - Investigates AI/ML and technology trends  
   - Produces concise research under `tech_research`

2. **HealthResearcher**
   - Explores medical breakthroughs and recent scientific advances  
   - Returns output under `health_research`

3. **FinanceResearcher**
   - Analyzes fintech and financial innovation trends  
   - Returns output under `finance_research`

4. **AggregatorAgent**
   - Runs *after* all research tasks complete  
   - Synthesizes the three reports into a single `executive_summary`

These sub-agents are grouped under a **ParallelAgent**, which executes all researchers concurrently.  
The ParallelAgent is then wrapped inside a **SequentialAgent**, ensuring that the aggregator runs *only after* all parallel subtasks complete.

### ✓ Example Workflow

~~~
User → TechResearcher + HealthResearcher + FinanceResearcher (parallel) → AggregatorAgent → Final Summary
~~~

This architecture is ideal when:

- tasks are **independent**
- speed and concurrency matter
- final output depends on combining multiple specialized results

### ✓ Runner

A dedicated development runner is provided:

~~~
uv run python -m adk_agent_parallel.main
~~~

This triggers:

- concurrent execution of three research agents  
- automatic aggregation of results  
- full debug trace output for transparent inspection

### ✓ Updated Directory Structure

`adk_agent_parallel/` includes:

- `agent.py` — orchestrator (SequentialAgent + ParallelAgent)
- `main.py` — local runner
- `sub_agents/`
  - `tech_researcher.py`
  - `health_researcher.py`
  - `finance_researcher.py`
  - `aggregator_agent.py`

All agents use the unified `.env` in the project root (introduced in v0.2.1).

---

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

These three sub-agents are wrapped by a `SequentialAgent` named **BlogPipeline**, ensuring predictable, ordered multi-agent behavior. Each agent automatically receives the previous agent’s output via ADK’s state injection.  No tools required - this module relies on the LLM's default capabilities to generate the outline, draft and editing.

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

# ▶️ Running the Multi-Agent Systems via integrated ADK GUI

### ADK Web UI
**This creates an interactive session where you can toggle between the various agent systems for testing**

~~~
uv run adk web --port 8000
~~~

Then open:

~~~
http://localhost:8000
~~~

Agents visible in the UI:
- `sample_agent`
- `adk_agent_loop`
- `adk_agent_multi`
- `adk_agent_parallel`
- `adk_agent_sequence`
- `adk_agent_single`

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