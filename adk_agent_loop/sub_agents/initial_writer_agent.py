from google.adk.agents import Agent
from common.llm import gemini_flash_lite

# This agent runs ONCE at the beginning to create the first draft.
initial_writer_agent = Agent(
    name="InitialWriterAgent",
    model=gemini_flash_lite(), #includes llm and retry logic imported from common/llm.py
    instruction="""Based on the user's prompt, write the first draft of a short story (around 100-150 words).
    Output only the story text, with no introduction or explanation.""",
    output_key="current_story",  # Stores the first draft in the state.
)