# FastAPI - Proyecto de aprendizaje

Este proyecto es una API desarrollada con FastAPI, creada con fines educativos para aprender y practicar el uso de este framework moderno de Python para el desarrollo de aplicaciones web y APIs.

## Características

- CRUD de películas (crear, leer, actualizar, eliminar)
- Uso de modelos Pydantic para validación de datos
- Ejemplo de parámetros de ruta y consulta
- Respuestas en formato JSON
- Documentación automática generada por FastAPI

## Endpoints principales

- `GET /` — Página de inicio simple
- `GET /movies` — Listar todas las películas
- `GET /movies/{id}` — Obtener una película por ID
- `GET /movies/?category=...` — Filtrar películas por categoría
- `POST /movies` — Crear una nueva película
- `PUT /movies/{id}` — Actualizar una película existente
- `DELETE /movies/{id}` — Eliminar una película

## Requisitos

- Python 3.10+
- FastAPI
- Uvicorn

Instalación de dependencias:
```bash
pip install fastapi uvicorn
```

## Ejecución

Para iniciar el servidor de desarrollo:
```bash
uvicorn main:app --reload
```

Accede a la documentación interactiva en:
- [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
- [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)

## Notas

- El proyecto utiliza una lista en memoria para almacenar las películas (no hay base de datos).
- El código y los ejemplos están comentados para facilitar el aprendizaje.