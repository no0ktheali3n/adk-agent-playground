from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import AgentTool
from google.genai import types

from .sub_agents.research_agent import research_agent
from .sub_agents.summarizer_agent import summarizer_agent

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.
root_agent = Agent(
    name="ResearchCoordinator",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config,
    ),
    instruction=(
        "You are a research coordinator. Your goal is to answer the user's "
        "query by orchestrating a workflow:\n"
        "1) Call the ResearchAgent tool to find relevant information.\n"
        "2) After receiving research_findings, call the SummarizerAgent tool "
        "to create a concise summary.\n"
        "3) Present the final_summary clearly to the user."
    ),
    # Sub-agents become callable tools:
    tools=[
        AgentTool(research_agent),
        AgentTool(summarizer_agent),
    ],
)