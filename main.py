"""
MCP Server - Servidor de Protocolo de Contexto de Modelo (Model Context Protocol)

Este servidor expone herramientas (tools) y prompts que pueden ser consumidos
por clientes MCP. Implementa funcionalidades de:
- Envío de correos electrónicos vía SMTP (Gmail)
- Prompts predefinidos para detección de intenciones y extracción de datos

Autor: MKevyn
Versión: 1.0.0
Fecha: Enero 2026
"""

# =============================================================================
# IMPORTACIONES
# =============================================================================
from fastmcp import FastMCP
from fastapi import FastAPI
from fastmcp.server.auth import StaticTokenVerifier
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
import os

# =============================================================================
# CONFIGURACIÓN DEL ENTORNO
# =============================================================================
# Cargar variables de entorno desde archivo .env para credenciales seguras
load_dotenv()

# Configuración del servidor SMTP de Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # Puerto para conexión TLS

# Credenciales de correo electrónico (obtenidas desde variables de entorno)
EMAIL_USER = os.getenv("EMAIL_USER")  # Dirección de correo del remitente
EMAIL_PASS = os.getenv("EMAIL_PASS")  # Contraseña de aplicación de Gmail

tokens = {
    "my-secret-token": {
        "client_id": "client_123",
        "scopes": ["read"]
    },
}

verifier = StaticTokenVerifier(tokens)

# Validación de credenciales al iniciar el servidor
if not EMAIL_USER or not EMAIL_PASS:
    print("⚠️ Advertencia: EMAIL_USER o EMAIL_PASS no están configurados en .env")
    print("   El envío de correos no funcionará hasta configurar estas variables.")

# =============================================================================
# INICIALIZACIÓN DEL SERVIDOR MCP
# =============================================================================
mcp = FastMCP("MCP Server",auth=verifier)
mcp_app = mcp.http_app()
api = FastAPI(lifespan=mcp_app.lifespan)

api.get("/api/status")
def status():
    return {"status": "ok"}

# =============================================================================
# HERRAMIENTAS (TOOLS) DEL SERVIDOR MCP
# =============================================================================
# Las herramientas son funciones que el cliente MCP puede invocar remotamente.
# Cada herramienta debe estar decorada con @mcp.tool() y retornar un resultado.

@mcp.tool(
    name="send_email",
    description="Envía un correo electrónico utilizando el servidor SMTP de Gmail. Soporta contenido HTML."
)
def send_email(to: str, subject: str, body: str) -> dict:
    """
    Envía un correo electrónico a través del servidor SMTP de Gmail.

    Esta herramienta permite enviar correos con contenido HTML, ideal para
    emails de bienvenida, notificaciones o comunicaciones personalizadas.

    Args:
        to (str): Dirección de correo del destinatario.
        subject (str): Asunto del correo electrónico.
        body (str): Contenido del correo en formato HTML.

    Returns:
        dict: Diccionario con el estado de la operación:
            - status: "success" si el envío fue exitoso
            - to: Dirección del destinatario
            - subject: Asunto del correo enviado

    Raises:
        SMTPException: Si ocurre un error durante el envío del correo.
    """
    # Crear el mensaje MIME con soporte para HTML
    msg = MIMEText(body, "html")
    msg['From'] = EMAIL_USER
    msg['To'] = to
    msg['Subject'] = subject

    # Establecer conexión segura con el servidor SMTP
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Iniciar conexión TLS segura
        server.login(EMAIL_USER, EMAIL_PASS)  # Autenticación
        server.sendmail(EMAIL_USER, [to], msg.as_string())  # Enviar correo

    return {"status": "success", "to": to, "subject": subject}

# =============================================================================
# PROMPTS DEL SERVIDOR MCP
# =============================================================================
# Los prompts son plantillas de texto que el cliente puede solicitar y usar
# para interactuar con modelos de lenguaje (LLM). Permiten centralizar
# la lógica de generación de prompts en el servidor.

@mcp.prompt(
    name="detect_action",
    description="Detecta la intención del usuario clasificándola en acciones predefinidas"
)
def detect_action(message: str) -> str:
    """
    Genera un prompt para clasificar la intención del mensaje del usuario.

    Este prompt instruye al LLM para analizar el mensaje y determinar
    qué acción desea realizar el usuario dentro del sistema.

    Args:
        message (str): Mensaje del usuario a clasificar.

    Returns:
        str: Prompt formateado para enviar al LLM.

    Acciones posibles:
        - 'saludo': El usuario está saludando o iniciando conversación.
        - 'informacion_productos': El usuario solicita información sobre productos.
    """
    return f"""
    Detecta la acción que el usuario quiere realizar:
    Existen dos tipos de acciones posibles: 'saludo' e 'informacion_productos'.

    Reglas de clasificación:
    - Si el usuario está saludando o iniciando conversación → acción: 'saludo'
    - Si el usuario solicita información sobre productos → acción: 'informacion_productos'

    Mensaje del usuario: '{message}'

    Responde ÚNICAMENTE con un JSON con el siguiente formato:
    {{"action": "<nombre_de_la_accion>"}}
    """

@mcp.prompt(
    name="client_info",
    description="Extrae nombre y correo electrónico del mensaje del usuario"
)
def client_info(message: str) -> str:
    """
    Genera un prompt para extraer información de contacto del usuario.

    Este prompt instruye al LLM para identificar y extraer el nombre
    y correo electrónico que el usuario haya proporcionado en su mensaje.

    Args:
        message (str): Mensaje del usuario que puede contener datos de contacto.

    Returns:
        str: Prompt formateado para enviar al LLM.

    Campos extraídos:
        - name: Nombre del cliente (null si no se proporciona)
        - email: Correo electrónico (null si no se proporciona)
    """
    return f"""
    Analiza el siguiente mensaje y extrae la información de contacto del usuario.

    Mensaje del usuario: '{message}'

    Instrucciones:
    - Busca un nombre propio en el mensaje
    - Busca una dirección de correo electrónico válida
    - Si no encuentras algún dato, usa null

    Responde ÚNICAMENTE con un JSON con el siguiente formato:
    {{"name": "<nombre_o_null>", "email": "<email_o_null>"}}
    """

@mcp.prompt(
    name="welcome_email",
    description="Genera un email de bienvenida personalizado con lista de productos"
)
def welcome_email(name: str, products: str) -> str:
    """
    Genera un prompt para crear un email de bienvenida personalizado.

    Este prompt instruye al LLM para generar un correo electrónico HTML
    profesional que incluya un saludo personalizado y una lista de productos.

    Args:
        name (str): Nombre del cliente para personalizar el saludo.
        products (str): Lista de productos disponibles (formato texto o JSON).

    Returns:
        str: Prompt formateado para enviar al LLM.

    Estructura del email generado:
        - Saludo personalizado con el nombre del cliente
        - Presentación de productos en formato lista HTML
        - Despedida cordial y profesional
    """
    return f"""
    Genera un email de bienvenida profesional para un nuevo cliente.

    Datos del cliente:
    - Nombre: {name}

    Productos disponibles:
    {products}

    Requisitos del email:
    1. Incluir un saludo cálido y personalizado con el nombre del cliente
    2. Presentar los productos en una lista HTML bien formateada
    3. Incluir una despedida cordial e invitación a contactar para más información
    4. El diseño debe ser limpio y profesional

    Responde ÚNICAMENTE con un JSON con el siguiente formato:
    {{"subject": "<asunto_del_email>", "body": "<contenido_html_del_email>"}}
    """


# =============================================================================
# PUNTO DE ENTRADA DEL SERVIDOR
# =============================================================================
# Iniciar el servidor MCP en modo HTTP para recibir conexiones de clientes
api.mount("/api", mcp_app)

if __name__ == "__main__":
    # print("🚀 Iniciando servidor MCP en http://localhost:8000/mcp")
    # mcp.run(transport="http", host="localhost", port=8000)
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8000)
