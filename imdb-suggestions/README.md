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

- Run fastapi docker Container and forward port 8000 to 8000: `$ docker run -p 8000:8000 python-fastapi`

- Access docker Container files: `docker exec -it {container-id} /bin/sh`


### Fast API

- Install dependencies `$ pip3 install fastapi uvcorn`
- Create `server.py` file
- Run api server via `$ python3 server.py`


### Credit

- Python Engineer on YouTube: https://youtu.be/bi0cKgmRuiA
