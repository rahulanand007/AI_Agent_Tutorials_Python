from .server import mcp_server

class MCPClient:
    def list_tools(self):
        return mcp_server.list_tool()
    def call_tools(self, tool_name:str, **kwargs):
        return mcp_server.execute(tool_name,**kwargs)

mcp_client = MCPClient()