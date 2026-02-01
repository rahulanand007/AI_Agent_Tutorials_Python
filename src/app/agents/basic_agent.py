from langchain.agents import create_agent
from src.app.core.llm import get_llm

from langchain.tools import tool


@tool
def echo(text: str) -> str:
    """Echo the input text."""
    return text


def create_basic_agent():
    llm = get_llm("gemini-2.5-flash")

    tools = [echo]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful assistant."
    )

    return agent