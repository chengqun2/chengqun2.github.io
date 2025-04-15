import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Configure parameters to connect to the MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"],
        env=None,
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("AI Chatbot is ready. Type 'exit' to quit.")
            while True:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    break

                # Call the 'chat' tool on the server
                result = await session.call_tool("chat", {"prompt": user_input})
                print("AI:", result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
