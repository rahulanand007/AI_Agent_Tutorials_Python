from fastapi import APIRouter
from pydantic import BaseModel
from src.app.agents.basic_agent import create_basic_agent
from src.app.agents.personal_chef_agent import chef_agent
from langchain_core.messages import HumanMessage

router = APIRouter(prefix="/agent", tags=["Agent"])


class AgentRequest(BaseModel):
    query: str


@router.post("/run")
def run_agent(request: AgentRequest):
    agent = create_basic_agent()
    result = agent.invoke({
        "messages":[HumanMessage(content=request.query)]
    })
    
    # Extract last AI message
    messages = result["messages"]
    final_message = messages[-1].content if messages else ""

    return {
        "response": final_message
    }

@router.post("/chef")
def run_chef_agent(request:AgentRequest):
    config = {"configurable": {"thread_id": "1"}}
    agent = chef_agent()
    result = agent.invoke({
        "messages":[HumanMessage(content=request.query)],
        config:config
    })

    messages = result["messages"]
    final_message = messages[-1].content if messages else ""
    return {
        "chef_response": final_message
    }