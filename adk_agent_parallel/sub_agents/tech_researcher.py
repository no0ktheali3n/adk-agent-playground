from google.adk.agents import Agent
from common.llm import gemini_flash_lite
from common.tools import google_search

# Tech Researcher: Focuses on AI and ML trends.
tech_researcher = Agent(
    name="TechResearcher",
    model=gemini_flash_lite(),
    instruction="""Research the latest AI/ML trends as of the current date. Include 3 key developments,
the main companies involved, and the potential impact. Keep the report very concise (100 words).""",
    tools=[google_search],
    output_key="tech_research",  # The result of this agent will be stored in the session state with this key.
)