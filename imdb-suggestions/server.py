import random
from typing import Optional
from fastapi import FastAPI
import uvicorn

from algo.get_imdb_top_movies import getImdbTopMovies

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}

@app.get("/movie-suggestions")
def move_suggestions():
  years, actors_list, titles, ratings = getImdbTopMovies()
  return {
    "years": years,
    "actors_list": actors_list,
    "titles": titles,
    "ratings": ratings,
  }

@app.get("/movie-suggestion")
def movie_suggestion():
  years, actors_list, titles, ratings = getImdbTopMovies()
  index = random.randrange(0, len(titles))
  return {
    "year": years[index],
    "actors_list": actors_list[index],
    "title": titles[index],
    "rating": ratings[index],
  }

uvicorn.run(app, port=8000, host='0.0.0.0', reload=True)
