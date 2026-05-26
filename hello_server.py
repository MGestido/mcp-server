from fastmcp import FastMCP

mcp = FastMCP("HelloServer")

@mcp.tool
def say_hello(name: str) -> str:
    """Says hello to the user."""
    return f"Hello my friend {name}!"