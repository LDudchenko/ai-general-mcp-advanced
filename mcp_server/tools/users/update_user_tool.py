from typing import Any

from mcp_server.models.user_info import UserUpdate
from mcp_server.tools.users.base import BaseUserServiceTool


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "update_user"

    @property
    def description(self) -> str:
        return "Update user"

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
                            "description": "The unique ID of the user to update."
                        },
                        "new_info": UserUpdate.model_json_schema()
                    },
                    "required": ["id", "new_info"]
                }
            }
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        user_id = arguments["id"]
        user_new_info = arguments["new_info"]
        user_update_request = UserUpdate.model_validate(user_new_info)
        return await self._user_client.update_user(user_id, user_update_request)
