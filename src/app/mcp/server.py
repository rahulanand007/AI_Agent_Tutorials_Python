from typing import Dict
from .schemas import MCPTool

class MCPServer:
    def __init__(self) -> None:
        self._tools: Dict[str, MCPTool] = {}

    def register_tool(self, tool:MCPTool) -> None:
        self._tools[tool.name] = tool

    def list_tool(self)-> Dict[str, MCPTool]:
        return self._tools
    
    def execute(self, tool_name:str, **kwargs):
        if tool_name not in self._tools:
            raise ValueError(f"Tool `{tool_name}` not found")
        
        return self._tools[tool_name].handler(**kwargs)
    
mcp_server = MCPServer()