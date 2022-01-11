# Dockerfile, Image, Container

FROM python:3.9

WORKDIR /fastap-app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./app ./app

CMD ["python3", "./app/server.py"]


# Running the imdb scraper algorithm on it's own:

# FROM python:3.9

# ADD main.py .

# RUN pip3 install requests beautifulsoup4

# CMD [ "python3", "./main.py" ]
