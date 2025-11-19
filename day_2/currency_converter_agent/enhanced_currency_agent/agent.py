from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from common.llm import gemini_flash_lite
from ..tools import get_fee_for_payment_method, get_exchange_rate
from .calculation_agent import calculation_agent

"""This enhanced agent uses another agent as a tool to generate code to calculate the final amount increasing calculation
accuracy.  We add our calculation_agent to the enhanced agent's toolset via AgentTool which allows our calculation_agent to
appear to our enhanced root agent as a callable tool."""

root_agent = LlmAgent(
    name="enhanced_currency_agent",
    model=gemini_flash_lite(),
    # Updated instruction
    instruction="""You are a smart currency conversion assistant. You must strictly follow these steps and use the available tools.

  For any currency conversion request:

   1. Get Transaction Fee: Use the get_fee_for_payment_method() tool to determine the transaction fee.
   2. Get Exchange Rate: Use the get_exchange_rate() tool to get the currency conversion rate.
   3. Error Check: After each tool call, you must check the "status" field in the response. If the status is "error", you must stop and clearly explain the issue to the user.
   4. Calculate Final Amount (CRITICAL): You are strictly prohibited from performing any arithmetic calculations yourself. You must use the calculation_agent tool to generate Python code that calculates the final converted amount. This 
      code will use the fee information from step 1 and the exchange rate from step 2.
   5. Provide Detailed Breakdown: In your summary, you must:
       * State the final converted amount.
       * Explain how the result was calculated, including:
           * The fee percentage and the fee amount in the original currency.
           * The amount remaining after deducting the fee.
           * The exchange rate applied.
    """,
    tools=[
        get_fee_for_payment_method,
        get_exchange_rate,
        AgentTool(agent=calculation_agent),  # Using another agent as a tool!
    ],
)