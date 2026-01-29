# Registro de Cambios (Changelog)

## [No publicado] - 2026-01-29

### Añadido
- **Test Server**: Se implementó la función `test_get_prompt` en `test_server.py` para verificar el correcto funcionamiento del prompt `client_info`.
- **Autenticación**: Se configuró `StreamableHttpTransport` en `test_server.py` para incluir el header `Authorization: Bearer my-secret-token`.

### Modificado
- **Test Server**: Se comentó la ejecución de `test_call_tool` para aislar las pruebas de los prompts.
- **Main Server**: (Inferred) Verificación de funcionalidades de prompts (`detect_action`, `client_info`, `welcome_email`).
