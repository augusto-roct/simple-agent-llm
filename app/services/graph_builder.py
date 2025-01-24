from langgraph.graph import StateGraph, START, END

from app.services.states import talker, search_on_web, route_agents
from app.models import State


graph_builder = StateGraph(State)

graph_builder.add_node("talker", talker)
graph_builder.add_node("search_on_web", search_on_web)

graph_builder.add_conditional_edges(
    "talker", route_agents, {"search_on_web": "search_on_web", END: END}
)

graph_builder.add_edge("search_on_web", "talker")
graph_builder.add_edge(START, "talker")

graph = graph_builder.compile()
