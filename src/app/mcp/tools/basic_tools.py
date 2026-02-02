from src.app.mcp.schemas import MCPTool
from src.app.mcp.server import mcp_server


def echo(text: str) -> str:
    return text


mcp_server.register_tool(
    MCPTool(
        name="echo",
        description="Echo the input text",
        handler=echo,
    )
)
