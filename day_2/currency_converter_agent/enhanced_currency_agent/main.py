import asyncio
from google.adk.runners import InMemoryRunner

# Import the orchestrator agent
from .agent import root_agent

from dotenv import load_dotenv

load_dotenv()

#helper function that prints the generated Python code and results from code execution tool so we can see calculations
def show_python_code_and_result(response):
    for i in range(len(response)):
        # Check if the response contains a valid function call result from the code executor
        if (
            (response[i].content.parts)
            and (response[i].content.parts[0])
            and (response[i].content.parts[0].function_response)
            and (response[i].content.parts[0].function_response.response)
        ):
            response_code = response[i].content.parts[0].function_response.response
            if "result" in response_code and response_code["result"] != "```":
                if "tool_code" in response_code["result"]:
                    print(
                        "Generated Python Code >> ",
                        response_code["result"].replace("tool_code", ""),
                    )
                else:
                    print("Generated Python Response >> ", response_code["result"])

#test runner for currency converter agent
async def main():
    print("🚀 Enhanced currency agent that uses custom tools and built-in code execution to calculate transaction fees and conversion rates to determine how much a user will receive from a given currency")
    print("----------------------------------------------------------")

    runner = InMemoryRunner(agent=root_agent)

    # give the currency agent an instruction to convert a currency and use custom-defined tools to determine output
    user_query = "Convert 1,250 USD to INR using a Bank Transfer. Show me the precise calculation."
    print(f"User > {user_query}\n")

    response = await runner.run_debug(user_query)

    print("Code execution:\n")
    show_python_code_and_result(response)

    #print("\nAssistant >")
    #print(response)

if __name__ == "__main__":
    asyncio.run(main())