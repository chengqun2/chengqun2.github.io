# server.py
import asyncio
import asyncpg
from contextlib import asynccontextmanager
from mcp.server.fastmcp import FastMCP

# Global variable for the database pool
db_pool = None

@asynccontextmanager
async def app_lifespan(server: FastMCP):
    """
    Asynchronous lifespan context that initializes and later closes
    a PostgreSQL connection pool.
    """
    global db_pool
    # Adjust the connection parameters as needed.
    db_pool = await asyncpg.create_pool(
        user='postgres',
        password='jsfr123456',  # Replace with your PostgreSQL password
        database='postgres',
        host='localhost',
        port=7184
    )
    try:
        yield
    finally:
        await db_pool.close()

# Create the MCP server instance with a lifespan handler.
mcp = FastMCP("ChatServer", lifespan=app_lifespan)

@mcp.tool()
async def send_message(username: str, message: str) -> str:
    """
    Store a chat message in PostgreSQL.
    
    Args:
        username: The name of the user sending the message.
        message: The chat message text.
    
    Returns:
        Confirmation that the message was sent.
    """
    async with db_pool.acquire() as connection:
        await connection.execute(
            "INSERT INTO messages(username, message) VALUES($1, $2)",
            username, message
        )
    return "Message sent."

@mcp.tool()
async def get_messages(limit: int = 10) -> str:
    """
    Retrieve the latest chat messages.
    
    Args:
        limit: Maximum number of messages to retrieve.
    
    Returns:
        A string listing the latest messages with timestamps.
    """
    async with db_pool.acquire() as connection:
        rows = await connection.fetch(
            "SELECT username, message, created_at FROM messages ORDER BY created_at DESC LIMIT $1",
            limit
        )
    if not rows:
        return "No messages found."
    # Format each row into a string line.
    response = "\n".join(
        f"[{row['created_at']}] {row['username']}: {row['message']}"
        for row in rows
    )
    return response

@mcp.resource("chat://instructions")
def chat_instructions() -> str:
    """
    A resource that provides chat instructions.
    """
    return ("Welcome to the Chat API.\n"
            "Use the 'send_message' tool to post a message and "
            "the 'get_messages' tool to view recent chat history.")

if __name__ == "__main__":
    print("123...")
    mcp.run()
    print("running...")
