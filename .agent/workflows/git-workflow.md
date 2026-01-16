---
description: Git workflow usando GitFlow y Conventional Commits con emojis
---

# 🌊 GitFlow + Conventional Commits

## Ramas Principales
- `main` - Código en producción
- `develop` - Rama de desarrollo/integración

## Ramas de Trabajo
- `feature/nombre-feature` - Nuevas funcionalidades
- `bugfix/nombre-bug` - Correcciones de bugs
- `hotfix/nombre-hotfix` - Correcciones urgentes en producción
- `release/v1.x.x` - Preparación de releases

## Formato de Commits (Conventional Commits + Emojis)

```
<emoji> <tipo>(<scope>): <descripción corta>

[cuerpo opcional]

[footer opcional]
```

## Tipos y Emojis

| Emoji | Tipo     | Descripción                           |
|-------|----------|---------------------------------------|
| ✨    | feat     | Nueva funcionalidad                   |
| 🐛    | fix      | Corrección de bug                     |
| 📝    | docs     | Cambios en documentación              |
| 💄    | style    | Formato, espacios, punto y coma, etc  |
| ♻️    | refactor | Refactorización de código             |
| ⚡    | perf     | Mejoras de rendimiento                |
| ✅    | test     | Añadir o modificar tests              |
| 🔧    | chore    | Tareas de mantenimiento               |
| 🏗️    | build    | Cambios en build/dependencias         |
| 👷    | ci       | Cambios en CI/CD                      |
| 🔥    | remove   | Eliminar código o archivos            |
| 🚀    | deploy   | Deploy a producción                   |
| 🎨    | art      | Mejorar estructura/formato código     |
| 🔒    | security | Correcciones de seguridad             |
| ⬆️    | upgrade  | Actualizar dependencias               |
| 🚧    | wip      | Trabajo en progreso                   |

## Ejemplos de Commits

```bash
# Nueva funcionalidad
git commit -m "✨ feat(auth): add JWT token validation"

# Corrección de bug
git commit -m "🐛 fix(api): resolve null pointer in user service"

# Documentación
git commit -m "📝 docs(readme): update installation instructions"

# Refactorización
git commit -m "♻️ refactor(prompts): simplify email template logic"

# Tests
git commit -m "✅ test(email): add unit tests for send_email function"
```

## Flujo de Trabajo

### 1. Crear feature branch
```bash
git checkout develop
git pull origin develop
git checkout -b feature/mi-nueva-feature
```

### 2. Hacer commits con convenciones
```bash
git add .
git commit -m "✨ feat(scope): descripción del cambio"
```

### 3. Push y Pull Request
```bash
git push origin feature/mi-nueva-feature
# Crear PR hacia develop
```

### 4. Merge a develop (después de code review)
```bash
git checkout develop
git merge --no-ff feature/mi-nueva-feature
git push origin develop
```

### 5. Release
```bash
git checkout -b release/v1.0.0 develop
# Preparar release, actualizar versión
git checkout main
git merge --no-ff release/v1.0.0
git tag -a v1.0.0 -m "🚀 Release v1.0.0"
git push origin main --tags
```
