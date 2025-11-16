import asyncio
import os

from agent.clients.custom_mcp_client import CustomMCPClient
from agent.clients.mcp_client import MCPClient
from agent.clients.openai_client import OpenAIClient
from agent.models.message import Message, Role


async def main():
    tools = []

    tool_clients: dict[str, MCPClient] = {}

    print("App started")
    ums_client = await MCPClient.create("http://localhost:8006/mcp")
    print("Initialized ums client")
    ums_tools = await ums_client.get_tools()
    for tool in ums_tools:
        tools.append(tool)
        tool_clients[tool.get('function', {}).get('name')] = ums_client
    print(f"UMS tools: {ums_tools}")

    remote_client = await MCPClient.create("https://remote.mcpservers.org/fetch/mcp")

    remote_tools = await remote_client.get_tools()
    print("Remote client")

    for tool in remote_tools:
        tools.append(tool)
        tool_clients[tool.get('function', {}).get('name')] = remote_client
    print(f"Remote client tools: {ums_tools}")

    openai_client = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4", tools=tools,
                                 tool_name_client_map=tool_clients)

    messages = [
        Message(
            role=Role.SYSTEM,
            content="You are an assistant that helps the user. Respond politely and use tools only when needed."
        )
    ]

    print("Chat started! Type 'exit' to stop.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        messages.append(Message(role=Role.USER, content=user_input))

        response = await openai_client.get_completion(messages)

        print("Assistant:", response.content)

        messages.append(response)


if __name__ == "__main__":
    asyncio.run(main())

# Check if Arkadiy Dobkin present as a user, if not then search info about him in the web and add him
