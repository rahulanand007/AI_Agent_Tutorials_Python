from langchain_core.tools import StructuredTool
from src.app.mcp.schemas import MCPTool


def to_langchain_tool(mcp_tool: MCPTool) -> StructuredTool:
    return StructuredTool.from_function(
        func=mcp_tool.handler,
        name=mcp_tool.name,
        description=mcp_tool.description,
    )
