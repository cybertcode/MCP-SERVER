# MCP Server - Servidor para envío de emails y prompts de usuario
from fastmcp import FastMCP
from dotenv import load_dotenv
import smtplib
import email
from email.mime.text import MIMEText
import os

# Cargar credenciales desde .env
load_dotenv()
SMTP_SERVER = "smtp.gmail.com"
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Inicializar servidor MCP
mcp = FastMCP("MCP Server")

# ==================== TOOLS ====================

@mcp.tool(name="send_email", description="Sends an email using SMTP.")
def send_email(to: str, subject: str, body: str) -> dict:
    """Envía un email via Gmail SMTP. Body puede ser HTML."""
    msg = MIMEText(body, "html")
    msg['From'] = EMAIL_USER
    msg['To'] = to
    msg['Subject'] = subject

    with smtplib.SMTP(SMTP_SERVER, 587) as server:
        server.starttls()  # Conexión segura
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, [to], msg.as_string())

    return {"status": "success", "to": to, "subject": subject}

# ==================== PROMPTS ====================

@mcp.prompt(name="detect_action", description="Detecta la acción que el usuario quiere realizar")
def detect_action(message: str) -> str:
    """Clasifica el mensaje en: 'saludo' o 'informacion_productos'"""
    return f"""
    Detecta la acción que el usuario quiere realizar:
    Existe dos tipos de acciones posibles; 'saludo',
    'informacion_productos'.
    - Si el usuario esta saludando, la accion es 'saludo'.
    - Si el usuario esta pidiendo información sobre productos, la acción es 'informacion_productos'.
    El mensaje del usuario es: '{message}'
    Responde con un json con los siguientes campos:
    - action: el nombre de la accion a realizar, puede ser 'saludo' o 'informacion_productos'
    """

@mcp.prompt(name="client_info", description="Comprueba si el usuario proporciona su nombre y correo electronico")
def client_info(message: str) -> str:
    """Extrae nombre y email del mensaje del usuario"""
    return f"""
    Comprueba si el usuario proporciona su nombre y correo. El mensaje del usuario es:
    '{message}'

    Responde con un json con los siguientes campos:
    - name (str | null): el nombre del cliente
    - email (str | null): el correo electronico del cliente
    """

@mcp.prompt(name="welcome_email", description="Genera un email de bienvenida para un nuevo cliente")
def welcome_email(name: str, products: list[dict]) -> str:
    """Genera prompt para crear email de bienvenida con lista de productos"""
    product_list = ""
    for product in products:
        product_list += f"{product['name']}: Price: {product['price']})\n"

    return f"""
    Genera un email de bienvenida para un nuevo cliente.
    El nombre del cliente es: {name}
    los productos disponibles son:
    {product_list}

    El email debe tener un saludo inicial, una presentacion de los productos en formato lista HTML,
    y una despedida cordial.

    Responde con el contenido del email en formato HTML.
    Devuelve tambien  el subject del email.
    La respuesta debe tener el siguiente formato JSON:
    - subject (str): "Asunto del email"
    - body (str): "Contenido del email en formato HTML"
    """

# Iniciar servidor en localhost:8000
mcp.run(transport="http", host="localhost", port=8000)
