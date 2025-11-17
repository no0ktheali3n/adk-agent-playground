from google.adk.agents import SequentialAgent

from .sub_agents.outline_agent import outline_agent
from .sub_agents.writer_agent import writer_agent
from .sub_agents.editor_agent import editor_agent

# Blog Pipeline: Orchestrates the blog post creation process.
root_agent = SequentialAgent(
    name="BlogPipeline",
    sub_agents=[outline_agent, writer_agent, editor_agent],
)