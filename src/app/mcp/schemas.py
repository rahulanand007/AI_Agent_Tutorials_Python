from pydantic import BaseModel
from typing import Callable

class MCPTool(BaseModel):
    name: str
    description: str
    handler: Callable