from app.models import InputAgent
from app.services import graph
from app.utils.config import SYSTEM_PROMPT


async def send_message(input_agent: InputAgent):
    """
    Send a message to the agent.
    """

    response = await graph.ainvoke(
        {
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": input_agent.message},
            ]
        }
    )

    for index in range(len(response["messages"])):
        message_dump = response["messages"][index].model_dump()

        fix_role = {"system": "system", "ai": "assistant", "human": "user"}

        role = message_dump["type"]
        role = fix_role[role]

        response["messages"][index] = {"role": role, "content": message_dump["content"]}

    return {"message": response["messages"][-1].content, "history": response}
