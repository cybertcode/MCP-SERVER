# Test Client para MCP Server - Requiere servidor corriendo en localhost:8000
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from mcp.types import CallToolResult, GetPromptResult
import asyncio

transport = StreamableHttpTransport(
    url="http://localhost:8000/mcp",
    headers={
        "Authorization": "Bearer my-secret-token"
    }
)
client = Client(transport=transport)
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
# tool_response: CallToolResult = asyncio.run(test_call_tool("send_email"))
# print("Tool Response:", tool_response.structured_content)

async def test_get_prompt():
    """Prueba la obtención del prompt 'client_info' enviando argumentos de prueba"""
    async with client:
        result = await client.get_prompt("client_info",{"message": "Hola, mi nombre es Kevyn y mi correo es kevyn_94@outlook.com"})
        return result
prompt_response: GetPromptResult = asyncio.run(test_get_prompt())
print("Prompt Response:", prompt_response.messages[0].content.text)
