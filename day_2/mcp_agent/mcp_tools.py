import uuid

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams, StreamableHTTPServerParams
from mcp import StdioServerParameters

from google.adk.apps.app import App, ResumabilityConfig
from google.adk.tools.function_tool import FunctionTool

# MCP integration with Everything Server
"""Behind the scenes:
        Server Launch: ADK runs npx -y @modelcontextprotocol/server-everything
        Handshake: Establishes stdio communication channel
        Tool Discovery: Server tells ADK: "I provide getTinyImage" functionality
        Integration: Tools appear in agent's tool list automatically
        Execution: When agent calls getTinyImage(), ADK forwards to MCP server
        Response: Server result is returned to agent seamlessly
    Why This Matters: You get instant access to tools without writing integration code!
    """
mcp_image_server = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",  # Run MCP server via npx
            args=[
                "-y",  # Argument for npx to auto-confirm install
                "@modelcontextprotocol/server-everything",
            ],
            tool_filter=["getTinyImage"],
        ),
        timeout=30,
    )
)

# kaggle mcp server for interacting with kaggle datasets, notebooks and competitions
"""What it provides:

    📊 Search and download Kaggle datasets
    📓 Access notebook metadata
    🏆 Query competition information etc.,

    Learn more: https://www.kaggle.com/docs/mcp (Kaggle MCP Documentation)"""
mcp_kaggle_server = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=[
                '-y',
                'mcp-remote',
                'https://www.kaggle.com/mcp'
            ],
        ),
        timeout=30,
    )
)

# github mcp server for PR/issue analysis
#mcp_github_server = McpToolset(
#    connection_params=StreamableHTTPServerParams(
#        url="https://api.githubcopilot.com/mcp/",
#        headers={
#            "Authorization": f"Bearer {GITHUB_TOKEN}",
#            "X-MCP-Toolsets": "all",
#            "X-MCP-Readonly": "true"
#        },
#    ),
#)