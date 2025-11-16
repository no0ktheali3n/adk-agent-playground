import asyncio
from google.adk.runners import InMemoryRunner

# Import the orchestrator agent
from .agent import root_agent

from dotenv import load_dotenv

load_dotenv()

#test runner for blog pipeline
async def main():
    print("🚀 Sequential Multi-Agent Runner: Outline + Writer + Editor")
    print("----------------------------------------------------------")

    runner = InMemoryRunner(agent=root_agent, app_name="adk_agent_sequence")

    # give the root agent an instruction to write blog post — it will orchestrate the sub-agents
    user_query = "Write a blog post about the benefits of multi-agent systems for software developers"
    print(f"User > {user_query}\n")

    response = await runner.run_debug(user_query)

    print("\nAssistant >")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())