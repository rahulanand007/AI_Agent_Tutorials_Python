from langchain.agents import create_agent
from src.app.core.llm import get_llm
from src.app.mcp.client import mcp_client
from src.app.mcp.langchain_adapter import to_langchain_tool


def create_basic_agent():
    llm = get_llm("gemini-2.5-flash")

    # Convert MCP tools → LangChain tools
    tools = [
        to_langchain_tool(tool)
        for tool in mcp_client.list_tools().values()
    ]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful assistant.",
    )

    return agent
