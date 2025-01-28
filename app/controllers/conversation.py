from app.models import InputAgent
from app.services import graph
from app.utils.config import SYSTEM_PROMPT


def get_history(input_agent: InputAgent):
    """
    Get the conversation history.
    """

    history = input_agent.model_dump()["history"]

    if not history:
        history = []

    history.insert(0, {"role": "system", "content": SYSTEM_PROMPT})

    history.append(
        {"role": "user", "content": input_agent.message},
    )

    return history


async def send_message(input_agent: InputAgent):
    """
    Send a message to the agent.
    """

    history = get_history(input_agent)

    response = await graph.ainvoke({"messages": history})

    for index in range(len(response["messages"])):
        message_dump = response["messages"][index].model_dump()

        if message_dump["type"] == "system":
            continue

        fix_role = {"ai": "assistant", "human": "user"}

        role = message_dump["type"]
        role = fix_role[role]

        response["messages"][index] = {"role": role, "content": message_dump["content"]}

    del response["messages"][0]

    return {
        "message": response["messages"][-1]["content"],
        "history": response["messages"],
    }
