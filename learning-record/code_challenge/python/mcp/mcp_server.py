from mcp.server.fastmcp import FastMCP

# Initialize the MCP server with a name
mcp = FastMCP("Simple Calculator")

# Define the addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    print("a:", a, "b:", b)
    return a + b

# Define the subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    return a - b

# Define the multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

# Define the division tool
@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Run the MCP server
if __name__ == "__main__":
    mcp.run()
