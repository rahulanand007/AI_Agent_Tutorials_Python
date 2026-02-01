import os
from langchain_openai import ChatOpenAI;
from langchain.agents import create_agent;
from dotenv import load_dotenv;

load_dotenv();

def get_llm(model_name: str):
    return ChatOpenAI(
        api_key=os.getenv("KNCKLABS_API_KEY"),
        base_url="https://admin.knacklabs.ai",
        model=model_name,
        temperature=0,
    )

# agent1 = create_agent(
#     "gpt-5-nano",
# )
