from typing import Any, Dict
from tavily import TavilyClient
from dotenv import load_dotenv
import os

from src.app.mcp.schemas import MCPTool
from src.app.mcp.server import mcp_server

load_dotenv()

tav_client = TavilyClient(os.getenv("TAVILY_API_KEY"))


def search_the_web(query: str) -> Dict[str, Any]:
    """Search the web for recipes and cooking information"""
    return tav_client.search(query=query)


mcp_server.register_tool(
    MCPTool(
        name="search_the_web",
        description="Search the web for recipes using ingredients",
        handler=search_the_web,
    )
)
