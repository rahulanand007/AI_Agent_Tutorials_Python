LangChain + MCP Agents Tutorial
===============================

A small FastAPI project for learning agent development with LangChain.
It includes:
- A general-purpose agent (`/agent/run`)
- A personal chef agent (`/agent/chef`)
- A lightweight MCP-style tool registry adapted to LangChain tools

Project Structure
-----------------
- `src/app/main.py` - FastAPI app bootstrap and tool registration imports
- `src/app/api/agent_routes.py` - HTTP routes for running agents
- `src/app/agents/basic_agent.py` - Basic assistant agent
- `src/app/agents/personal_chef_agent.py` - Chef-focused agent
- `src/app/core/llm.py` - Shared LLM client factory
- `src/app/mcp/server.py` - Tool registry/execution server
- `src/app/mcp/client.py` - Client wrapper for MCP server
- `src/app/mcp/langchain_adapter.py` - MCP tool -> LangChain tool adapter
- `src/app/mcp/tools/basic_tools.py` - `echo` tool registration
- `src/app/mcp/tools/chef_tools.py` - Tavily web search tool registration

Prerequisites
-------------
- Python 3.10-3.12 (project is configured for `<3.13`)
- `uv` package manager (`pip install uv`)

Environment Variables
---------------------
Create a `.env` file (or export env vars) with:

- `KNCKLABS_API_KEY` - API key used by `ChatOpenAI` client
- `TAVILY_API_KEY` - API key for Tavily web search tool

Example:
```env
KNCKLABS_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

Setup & Run
-----------
```bash
uv sync
uv run uvicorn src.app.main:app --reload
```

Server starts at `http://127.0.0.1:8000`.

API Endpoints
-------------
### Health Check
- `GET /`
- Response:
```json
{"status":"ok"}
```

### Run Basic Agent
- `POST /agent/run`
- Body:
```json
{"query":"Say hello and use tools if needed"}
```
- Response:
```json
{"response":"..."}
```

### Run Personal Chef Agent
- `POST /agent/chef`
- Body:
```json
{"query":"I have eggs, onion, and tomato. What can I cook?"}
```
- Response:
```json
{"chef_response":"..."}
```

cURL Examples
-------------
```bash
curl -X POST "http://127.0.0.1:8000/agent/run" \
  -H "Content-Type: application/json" \
  -d "{\"query\":\"Hello agent\"}"
```

```bash
curl -X POST "http://127.0.0.1:8000/agent/chef" \
  -H "Content-Type: application/json" \
  -d "{\"query\":\"I have paneer, spinach, garlic\"}"
```

How Tools Work
--------------
- Tools are registered in the MCP server (`mcp_server.register_tool(...)`).
- `main.py` imports tool modules so registration happens at startup.
- Agents fetch tools from MCP client and convert them via `StructuredTool`.

Notes / Limitations
-------------------
- Agent checkpointing uses `InMemorySaver` (ephemeral memory, process-local).
- `thread_id` is currently hardcoded to `"1"` in routes.
- If tool modules are not imported at startup, agents will have no tools.
- This project is for learning and local experimentation.
