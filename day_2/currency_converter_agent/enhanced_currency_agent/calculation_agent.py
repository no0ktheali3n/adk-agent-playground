from google.adk.agents import LlmAgent
from google.adk.runners import InMemoryRunner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search, AgentTool, ToolContext
from google.adk.code_executors import BuiltInCodeExecutor

from common.llm import gemini_flash_lite
from ..tools import get_fee_for_payment_method, get_exchange_rate

"""
The previous currency converter asked the agent to "calculate the final amount after fees, but LLMs aren't always
reliable with math.  They may make calculation errors or use inconsistent formulas.  In this enhanced implementation 
we attempt to solve this problem by asking our calculation_agent to generate a python code to do the math, run it, 
and give us the result using the built-in code executor.  Code execution is much more reliable than having the LLM 
doing the math in its "head."
"""
calculation_agent = LlmAgent(
    name="CalculationAgent",
    model=gemini_flash_lite(),
    instruction="""You are a specialized calculator that ONLY responds with Python code. You are forbidden from providing any text, explanations, or conversational responses.
 
     Your task is to take a request for a calculation and translate it into a single block of Python code that calculates the answer.
     
     **RULES:**
    1.  Your output MUST be ONLY a Python code block.
    2.  Do NOT write any text before or after the code block.
    3.  The Python code MUST calculate the result.
    4.  The Python code MUST print the final result to stdout.
    5.  You are PROHIBITED from performing the calculation yourself. Your only job is to generate the code that will perform the calculation.
   
    Failure to follow these rules will result in an error.
       """,
    code_executor=BuiltInCodeExecutor(),  # Use the built-in Code Executor Tool. This gives the agent code execution capabilities
)