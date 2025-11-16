from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class GetUserByIdTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "get_user_by_id"

    @property
    def description(self) -> str:
        return "Retrieve a user by their ID."

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "The unique numeric ID of the user to retrieve."
                        }
                    },
                    "required": ["id"]
                },
            },
        }
    async def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # 1. Get int `id` from arguments
        # 2. Call user_client get_user and return its results (it is async, don't forget to await)
        raise NotImplementedError()