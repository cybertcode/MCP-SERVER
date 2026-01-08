from fastmcp import FastMCP
from dotenv import load_dotenv
import smtplib
import email
from email.mime.text import MIMEText
import os
load_dotenv()
SMTP_SERVER = "smtp.gmail.com"
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

mcp = FastMCP("MCP Server")
@mcp.tool(
    name="send_email",
    description="Sends an email using SMTP.",
)
def send_email(
    to: str,
    subject: str,
    body: str)-> str:
    msg = MIMEText(body,"html")
    msg['From'] = EMAIL_USER
    msg['To'] = to
    msg['Subject'] = subject
    with smtplib.SMTP(SMTP_SERVER, 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, [to], msg.as_string())
    return {"status": "success","to": to,"subject": subject}

mcp.run(transport="http",host="localhost",port=8000)
