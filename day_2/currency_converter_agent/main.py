import asyncio
from google.adk.runners import InMemoryRunner

# Import the orchestrator agent
from .agent import root_agent

from dotenv import load_dotenv

load_dotenv()

#test runner for currency converter agent
async def main():
    print("🚀 Currency converter agent that uses custom tools to calculate transaction fees and conversion rates to determine how much a user will receive from a given currency")
    print("----------------------------------------------------------")

    runner = InMemoryRunner(agent=currency_agent)

    # give the currency agent an instruction to convert a currency and use custom-defined tools to determine output
    user_query = "I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?"
    print(f"User > {user_query}\n")

    response = await runner.run_debug(user_query)

    #print("\nAssistant >")
    #print(response)

if __name__ == "__main__":
    asyncio.run(main())