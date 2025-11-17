from google.adk.agents import Agent
from common.llm import gemini_flash_lite
from common.tools import google_search

# Health Researcher: Focuses on medical breakthroughs.
health_researcher = Agent(
    name="HealthResearcher",
    model=gemini_flash_lite(),
    instruction="""Research recent medical breakthroughs up to the current date. Include 3 significant advances,
their practical applications, and estimated timelines. Keep the report concise (100 words).""",
    tools=[google_search],
    output_key="health_research",  # The result will be stored with this key.
)