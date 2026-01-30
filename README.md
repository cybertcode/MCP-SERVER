# 🚀 MCP Server - Model Context Protocol

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)

**MCP Server** es una implementación robusta y eficiente de un servidor compatible con el *Model Context Protocol* (MCP). Diseñado para extender las capacidades de los Modelos de Lenguaje (LLMs), este servidor proporciona herramientas para el envío de correos electrónicos y prompts inteligentes para la detección de intenciones y gestión de datos de clientes.

---

## ✨ Características Principales

*   **📧 Integración SMTP Completa**: Envío de correos electrónicos enriquecidos (HTML) a través de Gmail u otros proveedores SMTP.
*   **🧠 Prompts Inteligentes**:
    *   **Detección de Intención**: Clasifica mensajes de usuarios automáticamente.
    *   **Extracción de Información**: Identifica datos clave como nombres y correos.
    *   **Generación de Contenido**: Crea emails de bienvenida personalizados dinámicamente.
*   **🔒 Seguridad Primero**: Gestión de credenciales mediante variables de entorno y validación de tokens.
*   **⚡ Alto Rendimiento**: Construido sobre **FastAPI** y **FastMCP** para una latencia mínima.

---

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

*   **Python 3.13** o superior.
*   **[uv](https://github.com/astral-sh/uv)**: Un gestor de paquetes de Python extremadamente rápido.

---

## 📦 Instalación

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/TUSUARIO/mcp-server.git
    cd mcp-server
    ```

2.  **Instalar dependencias:**

    Utilizando `uv` para sincronizar el entorno virtual:

    ```bash
    uv sync
    ```

---

## ⚙️ Configuración

1.  Crea un archivo `.env` en la raíz del proyecto basándote en el siguiente ejemplo:

    ```ini
    # .env
    EMAIL_USER=tu_correo@gmail.com
    EMAIL_PASS=tu_contraseña_de_aplicacion
    ```

    > **Nota:** Para Gmail, debes usar una "Contraseña de Aplicación" si tienes la verificación en dos pasos activada.

---

## 🚀 Uso

Para iniciar el servidor en modo desarrollo:

```bash
uv run main.py
```

El servidor estará disponible en: `http://0.0.0.0:8000`

### Endpoints Disponibles

| Tipo | Nombre | Descripción |
| :--- | :--- | :--- |
| **Tool** | `send_email` | Envía correos HTML vía SMTP. |
| **Prompt** | `detect_action` | Clasifica la intención del usuario (saludo/info). |
| **Prompt** | `client_info` | Extrae nombre y email de un texto. |
| **Prompt** | `welcome_email` | Genera el cuerpo de un email de bienvenida. |

---

## 📂 Estructura del Proyecto

```text
mcp-server/
├── main.py              # Punto de entrada y lógica del servidor
├── pyproject.toml       # Definición de dependencias
├── .gitignore           # Archivos ignorados por git
├── .env                 # Variables de entorno (NO COMMITEAR)
└── README.md            # Documentación del proyecto
```

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor, abre un *issue* o envía un *pull request* para mejoras o correcciones.

1.  Haz un Fork del proyecto.
2.  Crea tu rama de funcionalidad (`git checkout -b feature/AmazingFeature`).
3.  Haz Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`).
4.  Push a la rama (`git push origin feature/AmazingFeature`).
5.  Abre un Pull Request.

---

## 👤 Autor

**MKevyn**

---

<p align="center">
  <sub>Desarrollado con ❤️ y Python</sub>
</p>
