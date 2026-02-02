from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from src.app.core.llm import get_llm
from src.app.mcp.client import mcp_client
from src.app.mcp.langchain_adapter import to_langchain_tool


system_prompt = """
You are a personal chef.

The user gives ingredients they have.

Use available tools to search for recipes and cooking advice.
"""


def chef_agent():
    llm = get_llm("gemini-2.5-flash")

    tools = [
        to_langchain_tool(tool)
        for tool in mcp_client.list_tools().values()
    ]

    return create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
        checkpointer=InMemorySaver(),
    )
