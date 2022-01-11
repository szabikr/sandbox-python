from typing import Optional

from fastapi import FastAPI
import uvicorn

def getImdbTopMovies():
  print('not implemented')

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}

@app.get("/movie-suggestions")
def read_item():
  years, actors_list, titles, ratings = getImdbTopMovies()
  return {
    "years": years,
    "actors_list": actors_list,
    "titles": titles,
    "ratings": ratings,
  }

uvicorn.run(app, port=8000, host='0.0.0.0')
