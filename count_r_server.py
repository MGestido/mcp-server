from fastmcp import FastMCP

mcp = FastMCP("CountRServer")

@mcp.tool
def count_r(text: str) -> int:
    """Counts the number of 'r' letters (case-insensitive) in a word or phrase."""
    return text.lower().count("r")

if __name__ == "__main__":
    mcp.run()
