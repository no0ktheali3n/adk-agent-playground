import os
import asyncio
import base64
from google.adk.runners import InMemoryRunner

# Import the orchestrator agent
from .agent import root_agent

from dotenv import load_dotenv

load_dotenv()

#saves image to disk
def save_mcp_image(response, filename="tiny_image.png"):
    """
    Identify base64-encoded image content inside ADK/MCP responses
    and save it as a PNG file to disk.
    """
    for event in response:
        if getattr(event, "content", None) and getattr(event.content, "parts", None):
            for part in event.content.parts:

                # Tool response blocks
                if hasattr(part, "function_response") and part.function_response:

                    content_items = part.function_response.response.get("content", [])
                    for item in content_items:
                        if item.get("type") == "image":
                            # Decode base64 into raw bytes
                            img_bytes = base64.b64decode(item["data"])

                            # Resolve disk path
                            out_path = os.path.abspath(filename)

                            # Save PNG
                            with open(out_path, "wb") as f:
                                f.write(img_bytes)

                            return out_path

    return None  # No image found

#test runner for currency converter agent
async def main():
    print("🚀 Agent that integrates tool from MCP everything server to generate a tiny image")
    print("----------------------------------------------------------")

    runner = InMemoryRunner(agent=root_agent)

    # give the currency agent an instruction to convert a currency and use custom-defined tools to determine output
    user_query = "Provide a sample tiny image."
    print(f"User > {user_query}\n")

    response = await runner.run_debug(user_query, verbose=True)

    # Decode and save the MCP image
    image_path = save_mcp_image(response)

    if image_path:
        print(f"\n📁 Tiny image saved to: {image_path}")
    else:
        print("\n⚠️ No image detected in MCP response.")

if __name__ == "__main__":
    asyncio.run(main())