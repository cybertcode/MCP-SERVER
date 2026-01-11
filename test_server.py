# Test Client para MCP Server - Requiere servidor corriendo en localhost:8000
from fastmcp import Client
from mcp.types import CallToolResult, GetPromptResult
import asyncio

client = Client("http://localhost:8000/mcp")

async def test_call_tool(name: str) -> CallToolResult:
    """Llama a una herramienta del servidor MCP y retorna el resultado"""
    async with client:
        result = await client.call_tool(
            name,
            {
                "to": "kevyn_94@outlook.com",
                "subject": "Test Email",
                "body": "This is a test email sent from the MCP server"
            }
        )
        return result

# Ejecutar test y mostrar respuesta
tool_response: CallToolResult = asyncio.run(test_call_tool("send_email"))
print("Tool Response:", tool_response.structured_content)

