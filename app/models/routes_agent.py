from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class History(BaseModel):
    role: Literal["system", "assistant", "user"] = Field(
        ...,
        title="Role of the message",
        description="The role of the message. Only accept system, assistant or user",
    )
    content: str = Field(
        ...,
        title="Content of the message",
        description="The content of the message. Example: what the assistant said or what you said",
    )


class InputAgent(BaseModel):
    message: str = Field(
        ..., title="Message to agent", description="A message from the agent."
    )
    history: Optional[List[History]] = Field(
        None, title="History messages", description="A list of previous messages."
    )
