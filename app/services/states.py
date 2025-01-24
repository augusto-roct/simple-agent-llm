from googlesearch import search
from langgraph.graph import END

from app.models import State
from app.utils.config import structured_llm, SEARCH_PROMPT


async def talker(state: State):
    print("*" * 50 + " Node Talker " + "*" * 50)

    response = await structured_llm.ainvoke(state["messages"])
    response = response.model_dump()

    print(response, end="\n\n")

    return {
        "messages": [{"role": "assistant", "content": response["response"]}],
        "query_search": response["query_search"],
        "is_civil_engineering": response["is_civil_engineering"],
    }


def search_on_web(state: State):
    print("*" * 50 + " Node Search on web " + "*" * 50)

    search_results = list(
        search(state["query_search"], num_results=10, unique=True, advanced=True)
    )

    print(search_results, end="\n\n")

    return {
        "messages": [
            {
                "role": "assistant",
                "content": SEARCH_PROMPT.format(search_results=search_results),
            }
        ]
    }


def route_agents(state: State):
    print("*" * 50 + " Route Agents " + "*" * 50)

    print(state, end="\n\n")

    if state["is_civil_engineering"]:
        return END
    elif state["query_search"] and state["query_search"] != "":
        return "search_on_web"
    return END
