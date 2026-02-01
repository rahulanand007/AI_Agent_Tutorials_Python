LangChain Tutorial Server
=========================

Prerequisites
-------------
- Python 3.10+ (verified with 3.10 and 3.11)
- `uv` package manager installed globally (`pip install uv`)

Setup
-----
```
uv sync
uv run uvicorn src.app.main:app --reload
```

Notes
-----
- Export `KNACKLABS_API_KEY` in your environment to authenticate with the hosted LLM endpoint.
