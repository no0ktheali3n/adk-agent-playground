# common/llm.py
from google.genai import types
from google.adk.models.google_llm import Gemini

# One canonical retry config for the whole playground
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

def gemini_flash_lite() -> Gemini:
    """Standard Gemini 2.5 Flash-Lite model with our shared retry config."""
    return Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config,
    )