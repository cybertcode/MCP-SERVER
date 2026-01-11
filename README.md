# 📧 MCP Server - Servidor de Protocolo de Contexto de Modelo

Un servidor MCP (Model Context Protocol) construido con FastMCP que expone herramientas para envío de emails y prompts para interacción con usuarios.

## 📋 Tabla de Contenidos

- [¿Qué es MCP?](#-qué-es-mcp)
- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [API Reference](#-api-reference)

---

## 🤔 ¿Qué es MCP?

**MCP (Model Context Protocol)** es un protocolo abierto desarrollado por Anthropic que permite a los modelos de lenguaje (LLMs) interactuar con sistemas externos de manera segura y estructurada.

### Conceptos Clave:

| Concepto | Descripción |
|----------|-------------|
| **Tools** | Funciones que el modelo puede invocar para realizar acciones (ej: enviar emails) |
| **Prompts** | Plantillas de texto que guían al modelo en tareas específicas |
| **Resources** | Datos que el modelo puede leer (bases de datos, archivos, APIs) |

---

## ✨ Características

- 📨 **Envío de emails** via Gmail SMTP
- 🔍 **Detección de intención** del usuario
- 👤 **Extracción de datos** del cliente (nombre y email)
- ✉️ **Generación de emails** de bienvenida personalizados

---

## 📦 Requisitos

- Python 3.13+
- uv (gestor de paquetes)
- Cuenta de Gmail con contraseña de aplicación

---

## 🚀 Instalación

### 1. Clonar o descargar el proyecto

```bash
cd mcp-server
```

### 2. Instalar dependencias con uv

```bash
uv sync
```

Esto instalará automáticamente:
- `fastmcp>=2.14.2`
- `python-dotenv>=1.2.1`

---

## ⚙️ Configuración

### 1. Configurar credenciales de Gmail

Crea o edita el archivo `.env` en la raíz del proyecto:

```env
EMAIL_USER=tu_email@gmail.com
EMAIL_PASS=xxxx xxxx xxxx xxxx
```

### 2. Obtener contraseña de aplicación de Gmail

> ⚠️ **Importante**: No uses tu contraseña normal de Gmail. Necesitas una "Contraseña de Aplicación".

1. Ve a [Configuración de Seguridad de Google](https://myaccount.google.com/security)
2. Activa la **Verificación en 2 pasos**
3. Ve a "Contraseñas de aplicaciones"
4. Genera una nueva contraseña para "Correo" en "Dispositivo Windows"
5. Copia la contraseña de 16 caracteres (sin espacios) al archivo `.env`

---

## 🎮 Uso

### Iniciar el servidor

```bash
uv run main.py
```

El servidor se iniciará en `http://localhost:8000`

### Probar el servidor

Con el servidor corriendo en otra terminal:

```bash
uv run test_server.py
```

Esto enviará un email de prueba y mostrará la respuesta del servidor.

---

## 📁 Estructura del Proyecto

```
mcp-server/
├── .env                 # Variables de entorno (credenciales)
├── .gitignore           # Archivos ignorados por git
├── .python-version      # Versión de Python (3.13)
├── main.py              # Servidor MCP principal
├── test_server.py       # Cliente de prueba
├── pyproject.toml       # Configuración del proyecto y dependencias
├── uv.lock              # Lock file de dependencias
└── README.md            # Esta documentación
```

---

## 📚 API Reference

### Tools (Herramientas)

#### `send_email`

Envía un email usando SMTP de Gmail.

**Parámetros:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `to` | `str` | Email del destinatario |
| `subject` | `str` | Asunto del email |
| `body` | `str` | Contenido HTML del email |

**Retorna:**

```json
{
  "status": "success",
  "to": "destinatario@email.com",
  "subject": "Asunto del email"
}
```

---

### Prompts

#### `detect_action`

Detecta la intención del usuario (saludo o información de productos).

**Parámetros:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `message` | `str` | Mensaje del usuario a analizar |

**Respuesta esperada del modelo:**

```json
{
  "action": "saludo" | "informacion_productos"
}
```

---

#### `client_info`

Extrae nombre y email del mensaje del usuario.

**Parámetros:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `message` | `str` | Mensaje del usuario |

**Respuesta esperada del modelo:**

```json
{
  "name": "Nombre del cliente" | null,
  "email": "email@ejemplo.com" | null
}
```

---

#### `welcome_email`

Genera un email de bienvenida personalizado.

**Parámetros:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `name` | `str` | Nombre del cliente |
| `products` | `list[dict]` | Lista de productos `[{"name": "...", "price": ...}]` |

**Respuesta esperada del modelo:**

```json
{
  "subject": "Asunto del email",
  "body": "<html>...</html>"
}
```

---

## 🔗 Integración con Clientes MCP

Este servidor puede ser consumido por cualquier cliente compatible con MCP, incluyendo:

- **Claude Desktop** - Configura en `claude_desktop_config.json`
- **Otros LLMs** - Cualquier cliente que implemente el protocolo MCP

### Ejemplo de configuración para Claude Desktop:

```json
{
  "mcpServers": {
    "mcp-server": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

---

## 📝 Licencia

MIT License

---

## 👤 Autor

Desarrollado por MKEVYN
