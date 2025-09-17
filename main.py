from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi primera API con FastAPI"
#app.version = "1.0.1" # Se puede definir la versión de la API manualmente

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": 2009,
        "rating": 7.9,
        "category": "Acción"
    }
]

@app.get("/", tags=["Home"])
def home():
    return "Hola mundo"

# @app.get("/", tags=["Home"])
# 'tags' es opcional y sirve para poner nombre a las rutas en la documentación
# también se puede usar para agrupar rutas similares con el mismo tag

@app.get("/movies", tags=["Home"])
def home():
    #return HTMLResponse('<h1>Hola mundo</h1>')
    return movies

