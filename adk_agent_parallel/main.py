import asyncio
from google.adk.runners import InMemoryRunner

# Import the orchestrator agent
from .agent import root_agent

from dotenv import load_dotenv

load_dotenv()

#test runner for parallel tech, health and finance research reporters and sequential aggregated summarizer
async def main():
    print("🚀 Parallel Multi-Agent Runner: Runs Tech, Health and Finance Research Agents in parallel, then aggregates results into executive summary")
    print("----------------------------------------------------------")

    runner = InMemoryRunner(agent=root_agent, app_name="adk_agent_parallel")

    # give the root agent an instruction to research delegated researcher topics — it will orchestrate the sub-agents to work in parallel before returning reports to aggregator for final executive summary
    user_query = "Run the daily executive briefing on Tech, Health, and Finance"
    print(f"User > {user_query}\n")

    response = await runner.run_debug(user_query)

    #print("\nAssistant >")
    #print(response)

if __name__ == "__main__":
    asyncio.run(main())