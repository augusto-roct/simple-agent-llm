from pydantic import BaseModel, Field
from typing import List


class InputAgent(BaseModel):
    message: str = Field(
        ..., title="Message to agent", description="A message from the agent."
    )
    history: List[str] = Field(
        ..., title="History messages", description="A list of previous messages."
    )
