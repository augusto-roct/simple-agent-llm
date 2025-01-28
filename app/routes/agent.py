from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from app.models import InputAgent
from app.controllers.conversation import send_message

agent_blueprint = Blueprint("agent", __name__)


@agent_blueprint.route("/", methods=["POST"])
async def talk_with_agent():
    """
    This endpoint accepts a POST request to receive messages from the agent.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            message:
              type: string
              required: true
              description: A message from the agent.
            history:
              type: array
              required: False
              items:
                type: object
                properties:
                  role:
                    type: string
                    description: The role of the message.
                  content:
                    type: string
                    description: The content of the message.
              description: A list of previous messages.
    responses:
      200:
        description: Valid input
        schema:
          type: object
          properties:
            message:
              type: string
            data:
              type: object
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: array
              items:
                type: object
    """

    try:
        agent_talker = InputAgent.model_validate(request.json)

        response = await send_message(agent_talker)

        return jsonify(
            {"message": "Request processed successfully", "data": response}
        ), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
