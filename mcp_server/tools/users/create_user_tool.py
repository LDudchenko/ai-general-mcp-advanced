from typing import Any

from mcp_server.models.user_info import UserCreate
from mcp_server.tools.users.base import BaseUserServiceTool


class CreateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "add_user"

    @property
    def description(self) -> str:
        return "Creates a user using the provided UserCreate data."

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": UserCreate.model_json_schema(),
            },
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        user_data = UserCreate.model_validate(arguments)
        created_user = await self._user_client.add_user(user_data)
        return created_user