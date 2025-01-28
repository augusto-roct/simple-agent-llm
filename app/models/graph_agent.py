from pydantic import BaseModel, Field
from typing import Annotated, Optional, TypedDict

from langgraph.graph.message import add_messages


class AgentTalker(BaseModel):
    """Interface for the agent to talk to the user"""

    response: str = Field(description="The response from the agent")
    is_civil_engineering: bool = Field(
        description="Is the query related to civil engineering?"
    )
    query_search: Optional[str] = Field(
        description="The query to search on the web, if is necessary to asnwer the user"
    )


class State(TypedDict):
    messages: Annotated[list, add_messages]
    query_search: Optional[str]
    is_civil_engineering: bool
