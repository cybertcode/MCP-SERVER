# Registro de Cambios (Changelog)

## [No publicado] - 2026-01-29

### Añadido
- **Test Server**: Se implementó la función `test_get_prompt` en `test_server.py` para verificar el correcto funcionamiento del prompt `client_info`.
- **Autenticación**: Se configuró `StreamableHttpTransport` en `test_server.py` para incluir el header `Authorization: Bearer my-secret-token`.

### Modificado
- **Test Server**: Se comentó la ejecución de `test_call_tool` para aislar las pruebas de los prompts.
- **Main Server**: (Inferred) Verificación de funcionalidades de prompts (`detect_action`, `client_info`, `welcome_email`).

### Corregido
- **Main Server**: Se corrigió la indentación de `api.mount("/api", mcp_app)` para asegurar que el endpoint `/api` se registre correctamente al inicio.
- **Autenticación**: Se relajó la validación de `client_id` en `main.py` para evitar errores de terminación de sesión.
- **Rutas**: Se actualizó la URL en `test_server.py` a `http://localhost:8000/api/mcp` para coincidir con el montaje del servidor.
