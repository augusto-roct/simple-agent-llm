# Simple Agent LLM

This API provides access to a generative AI agent that can converse on a wide range of topics, with one exception: it **cannot** discuss civil engineering. If the agent does not know how to respond to a question, it will perform a quick search of the top 10 Google results and use that information to generate a response.

---

## Getting Started

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --interface wsgi --host 0.0.0.0 --port 8080
```

Open Swagger:

```
localhost:8080/apidocs
```

## Overview

- **Endpoint**: `/api/v1/agent`
- **Method**: `POST`
- **Content-Type**: `application/json`

### Request Body

| Field   | Type     | Required | Description                                                                                                                                       |
| ------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| message | `string` | Yes      | The user's question or message to the AI agent.                                                                                                   |
| history | `array`  | No       | A list of previous messages for context. Each item contains `role` (e.g., "user" or "assistant") and `content`. Helps maintain conversation flow. |

**Example**:

```json
{
  "message": "Hello, how are you?",
  "history": [
    {
      "role": "user",
      "content": "Hi!"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I help you today?"
    }
  ]
}
```

### Response Body

| Field   | Type     | Description                                                                                                                                       |
| ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| message | `string` | The AI agent's final response to the user. agent.                                                                                                 |
| history | `array`  | A list of previous messages for context. Each item contains `role` (e.g., "user" or "assistant") and `content`. Helps maintain conversation flow. |

### Topics

The AI agent can discuss any topic except civil engineering.
If a question is related to civil engineering, the agent responds with a statement that it cannot converse on that subject.

### Unknown Responses

If the agent does not know how to answer, it will perform a quick search of the top 10 Google results.
It then uses the information from those results to formulate a reply.

### Error Handling

If the request body is invalid, a 400 status code is returned with details in the error field.
Always provide a valid message field to ensure a successful request.
