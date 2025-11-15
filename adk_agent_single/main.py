import asyncio
import os

from google.adk.runners import InMemoryRunner

# agent config
from agent import root_agent

# local env
from dotenv import load_dotenv

load_dotenv()

try:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    print("✅ Gemini API key setup complete.")
except Exception as e:
    print(
        f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your environment secrets. Details: {e}"
    )

async def main():
    print("Hello from adk-agent-single!")
    runner = InMemoryRunner(agent=root_agent, app_name="agents")
    response = await runner.run_debug("What's the time and weather in Greensboro, North Carolina right now?")
    # print debug response to console
    #print(response)


if __name__ == "__main__":
    asyncio.run(main())
