from google.adk.agents import ParallelAgent, SequentialAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.genai import types

from .sub_agents.finance_researcher import finance_researcher
from .sub_agents.health_researcher import health_researcher
from .sub_agents.tech_researcher import tech_researcher
from .sub_agents.aggregator_agent import aggregator_agent

# retry logic
retry_config = types.HttpRetryOptions(
    attempts=5,        # Maximum retry attempts
    exp_base=7,        # Delay multiplier
    initial_delay=1,   # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

# The ParallelAgent runs all its sub-agents simultaneously, nested inside of a SequentialAgent.
parallel_research_team = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[tech_researcher, health_researcher, finance_researcher],
)

# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
root_agent = SequentialAgent(
    name="ResearchSystem",
    sub_agents=[parallel_research_team, aggregator_agent],
)