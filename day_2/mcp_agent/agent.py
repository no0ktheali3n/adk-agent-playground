from google.adk.agents import LlmAgent

from common.llm import gemini_flash_lite

from .mcp_tools import mcp_image_server

# Create image agent with MCP integration
root_agent = LlmAgent(
    model=gemini_flash_lite(),
    name="image_agent",
    instruction="Use the MCP Tool to generate images for user queries",
    tools=[mcp_image_server],
)