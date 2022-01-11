# imdb-suggestions

- Importing imdb scraper code from https://github.com/python-engineer/python-fun/blob/master/moviepicker/main.py
- Create virtual environment
- Resolve the dependencies
- Freeze the dependencies via running: `$ pip3 freeze > requirements.txt`
- Run `$ python3 main.py` and get your movies suggestion

### Dockerizing

- Write `Dockerfile`
- Build `python-imbd` docker Image `$ docker build -t python-imdb .`

_without interactive mode_
- Run docker Container `$ docker run python-imdb`

_with interactive mode_
- Run docker Container `$ docker run -t -i python-imdb` where `-t` is for terminal and `-i` for interactive mode

### Fast API

- Install dependencies `$ pip3 install fastapi uvcorn`
- Create `app/server.py` file
- Run api server via `$ python3 app/server.py`


### Credit

- Python Engineer on YouTube: https://youtu.be/bi0cKgmRuiA
