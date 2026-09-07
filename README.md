# Pipeline CI/CD con Testing Automatizado de APIs y Quality Gates

Proyecto orientado al aseguramiento de la calidad de software continuo (QA) y entrega continua (CI/CD) para una API REST construida con **FastAPI**. El pipeline automatiza la ejecución de pruebas unitarias y de integración, el análisis estático de código (SAST), la validación de umbrales de calidad mediante **Quality Gates** bloqueantes, la contenerización con **Docker** y el despliegue automático.

---

## 🚀 Arquitectura y Tecnologías

* **Backend / API:** Python 3.10, FastAPI, Uvicorn.
* **Testing Automatizado:** pytest, TestClient (httpx), Coverage.py.
* **Calidad de Código y SAST:** Flake8 (linter PEP8), SonarCloud.
* **CI/CD:** GitHub Actions.
* **Contenerización:** Docker, Docker Compose.
* **ChatOps & Notificaciones:** Slack Webhooks, Trello API.
* **Despliegue:** Render Cloud.

---

## ⚙️ Flujo del Pipeline (GitHub Actions)

El workflow se activa ante cada `push` o `pull_request` sobre la rama `main` y ejecuta las siguientes fases de forma secuencial:

1. **Linting & Análisis Estático:** Validación de estilo y buenas prácticas de código con `flake8`.
2. **Ejecución de Pruebas & Cobertura:** Ejecución de suites de prueba con `pytest` y generación del reporte de cobertura `coverage.xml`.
3. **Análisis de Seguridad y Calidad (SonarCloud):** Escaneo de vulnerabilidades, bugs, code smells y cálculo de cobertura de código.
4. **Quality Gate Bloqueante:** Consulta activa mediante API a SonarCloud. Si el estado del Quality Gate no es `OK`, el pipeline se interrumpe y se notifica el fallo vía Slack.
5. **Docker Build:** Construcción y validación de la imagen de contenedor.
6. **Despliegue Continuo (CD):** Ante la aprobación estricta de todos los controles de calidad, se dispara el despliegue automático hacia Render.

---

## 🛠️ Ejecución Local con Docker

Para correr el proyecto o sus pruebas en un entorno aislado sin necesidad de configurar Python localmente:

### Requisitos previos
* Docker y Docker Desktop instalados y en ejecución.

### 1. Ejecutar la suite de pruebas automáticas
```bash
docker compose run --rm test
