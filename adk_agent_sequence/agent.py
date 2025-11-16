from google.adk.agents import SequentialAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.genai import types

from .sub_agents.outline_agent import outline_agent
from .sub_agents.writer_agent import writer_agent
from .sub_agents.editor_agent import editor_agent

# retry logic
retry_config = types.HttpRetryOptions(
    attempts=5,        # Maximum retry attempts
    exp_base=7,        # Delay multiplier
    initial_delay=1,   # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

# Blog Pipeline: Orchestrates the blog post creation process.
root_agent = SequentialAgent(
    name="BlogPipeline",
    sub_agents=[outline_agent, writer_agent, editor_agent],
)