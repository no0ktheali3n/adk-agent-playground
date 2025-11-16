import asyncio
from google.adk.runners import InMemoryRunner

# Import the orchestrator agent
from .agent import root_agent

from dotenv import load_dotenv

load_dotenv()

#test runner for blog pipeline
async def main():
    print("🚀 Parallel Multi-Agent Runner: Runs Tech, Health and Finance Research Agents in parallel, then aggregates results into executive summary")
    print("----------------------------------------------------------")

    runner = InMemoryRunner(agent=root_agent, app_name="adk_agent_parallel")

    # give the root agent an instruction to write blog post — it will orchestrate the sub-agents
    user_query = "Run the daily executive briefing on Tech, Health, and Finance"
    print(f"User > {user_query}\n")

    response = await runner.run_debug(user_query)

    #print("\nAssistant >")
    #print(response)

if __name__ == "__main__":
    asyncio.run(main())