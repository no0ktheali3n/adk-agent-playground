import asyncio
from google.adk.runners import InMemoryRunner

# Import the orchestrator agent
from .agent import root_agent

from dotenv import load_dotenv

load_dotenv()

async def main():
    print("🚀 Multi-Agent Runner: Research + Summarizer + Coordinator")
    print("----------------------------------------------------------")

    runner = InMemoryRunner(agent=root_agent, app_name="adk_agent_multi")

    # Ask the root agent a question — it will orchestrate the sub-agents
    user_query = "What are the latest advancements in quantum computing and what do they mean for AI?"
    print(f"User > {user_query}\n")

    response = await runner.run_debug(user_query)

    print("\nAssistant >")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
