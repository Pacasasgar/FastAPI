from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

app = FastAPI()

app.title = "Mi primera API con FastAPI"
#app.version = "1.0.1" # Se puede definir la versión de la API manualmente

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    overview: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None
    category: Optional[str] = None

class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15, default="My Movie") # default es opcional
    overview: str = Field(min_length=5, max_length=50, default="My Overview")
    year: int = Field(le=datetime.date.today().year, ge=1900) # le = less than or equal to
    rating: float = Field(le=10, ge=0) # ge = greater than or equal to
    category: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "My Movie",
                "overview": "My Overview",
                "year": 2023,
                "rating": 7.5,
                "category": "Action"
            }
        }
    } # Se usa como valor por defecto en la documentación de la API

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": 2009,
        "rating": 7.9,
        "category": "Acción"
    }
    ,{
        "id": 2,
        "title": "I Am Legend",
        "overview": "Año 2012. Un virus ha convertido a la mayoría de la población mundial en ...",
        "year": 2007,
        "rating": 7.2,
        "category": "Ciencia Ficción"
    }
    ,{
        "id": 3,
        "title": "300",
        "overview": "Basada en la novela gráfica de Frank Miller, narra la historia de la Batalla de ...",
        "year": 2006,
        "rating": 7.7,
        "category": "Acción"
    }
    ,{
        "id": 4,
        "title": "The Avengers",
        "overview": "Loki, el hermano adoptivo del dios Thor, ha llegado a la Tierra con un ejército ...",
        "year": 2012,
        "rating": 8.1,
        "category": "Acción"
    }
]

@app.get("/", tags=["Home"])
def home():
    #return HTMLResponse('<h1>Hola mundo</h1>')
    return "Hola mundo"

# @app.get("/", tags=["Home"])
# 'tags' es opcional y sirve para poner nombre a las rutas en la documentación
# también se puede usar para agrupar rutas similares con el mismo tag

@app.get("/movies", tags=["Movies"])
def get_movies() -> List[Movie]:
    return movies

@app.get("/movies/{id}", tags=["Movies"]) # Path Parameter
def get_movie(id: int) -> Movie:
   for movie in movies:
       if movie["id"] == id:
           return movie
   return []

@app.get("/movies/", tags=["Movies"]) # Query Parameter
def get_movie_by_category(category: str) -> List[Movie]:
    for movie in movies:
       if movie["category"] == category:
           return movie
    return []

@app.post("/movies", tags=["Movies"])
def create_movie(movie: MovieCreate) -> Movie:
    movies.append(movie.model_dump()) # model_dump() convierte el objeto movie en un diccionario
    return movies[-1] # Devuelve la última película añadida

@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for item in movies:
        if item["id"] == id:
            item ["title"] = movie.title
            item ["overview"] = movie.overview
            item ["year"] = movie.year
            item ["rating"] = movie.rating
            item ["category"] = movie.category
    return movies

@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return movies