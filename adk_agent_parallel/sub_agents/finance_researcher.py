from google.adk.agents import Agent
from common.llm import gemini_flash_lite
from common.tools import google_search

# Finance Researcher: Focuses on fintech trends.
finance_researcher = Agent(
    name="FinanceResearcher",
    model=gemini_flash_lite(),
    instruction="""Research current fintech trends for the current date. Include 3 key trends,
their market implications, and the future outlook. Keep the report concise (100 words).""",
    tools=[google_search],
    output_key="finance_research",  # The result will be stored with this key.
)