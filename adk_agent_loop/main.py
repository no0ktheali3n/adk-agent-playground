import asyncio
from google.adk.runners import InMemoryRunner

# Import the orchestrator agent
from .agent import root_agent

from dotenv import load_dotenv

load_dotenv()

#test runner for short story writer / refiner / critic loop
async def main():
    print("🚀 Multi-Agent Loop Runner: Writes a short story and refines in a loop until approved by critic")
    print("----------------------------------------------------------")

    runner = InMemoryRunner(agent=root_agent, app_name="adk_agent_parallel")

    # give the root agent an instruction to write a short story — it will orchestrate the refinement loop and sequential sub-agents
    user_query = "Write a short story about a lighthouse keeper who discovers a mysterious, glowing map"
    print(f"User > {user_query}\n")

    response = await runner.run_debug(user_query)

    #print("\nAssistant >")
    #print(response)

if __name__ == "__main__":
    asyncio.run(main())