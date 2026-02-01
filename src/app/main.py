from fastapi import FastAPI
from src.app.api.agent_routes import router as agent_router

app = FastAPI(title="LangChain Tutorial Server")

app.include_router(agent_router)


@app.get("/")
def health_check():
    return {"status": "ok"}