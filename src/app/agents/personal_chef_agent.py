from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
from typing import Any, Dict
from langgraph.checkpoint.memory import InMemorySaver  
import os

from src.app.core.llm import get_llm

load_dotenv();

tav_client = TavilyClient(os.getenv("TAVILY_API_KEY"));

@tool
def search_the_web(query:str) -> Dict[str, Any]:
    """Search the web for information"""
    return tav_client.search(query=query)

system_prompt = """

You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""

def chef_agent():
    llm= get_llm("gemini-2.5-flash")
    chef = create_agent(
        model=llm,
        tools= [search_the_web],
        system_prompt=system_prompt,
        checkpointer=InMemorySaver()
    )
    return chef


