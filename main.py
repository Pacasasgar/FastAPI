from fastapi import FastAPI, Body
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
def get_movies():
    return movies

@app.get("/movies/{id}", tags=["Movies"]) # Path Parameter
def get_movie(id: int):
   for movie in movies:
       if movie["id"] == id:
           return movie
   return []

@app.get("/movies/", tags=["Movies"]) # Query Parameter
def get_movie_by_category(category: str):
    for movie in movies:
       if movie["category"] == category:
           return movie
    return []

@app.post("/movies", tags=["Movies"])
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
    ):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies[-1] # Devuelve la última película añadida

@app.put("/movies/{id}", tags=["Movies"])
def update_movie(
    id: int,
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
    ):
    for movie in movies:
        if movie["id"] == id:
            movie ["title"] = title
            movie ["overview"] = overview
            movie ["year"] = year
            movie ["rating"] = rating
            movie ["category"] = category
    return movies

@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return movies