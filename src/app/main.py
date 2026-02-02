from fastapi import FastAPI
from src.app.api.agent_routes import router as agent_router


from src.app.mcp.tools import basic_tools  
from src.app.mcp.tools import chef_tools  

app = FastAPI(title="LangChain + MCP")

app.include_router(agent_router)


@app.get("/")
def health_check():
    return {"status": "ok"}