from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "search_users"

    @property
    def description(self) -> str:
        return "Search users by name"

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "User's first name to search for (optional)."
                },
                "surname": {
                    "type": "string",
                    "description": "User's last name to search for (optional)."
                },
                "email": {
                    "type": "string",
                    "description": "User's email address to search for (optional)."
                },
                "gender": {
                    "type": "string",
                    "description": "User's gender to search for (optional, e.g., 'male' or 'female')."
                }
            },
            "required": []
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        return await self._user_client.search_users(**arguments)
