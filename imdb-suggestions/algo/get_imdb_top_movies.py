import requests
from bs4 import BeautifulSoup

URL = 'http://www.imdb.com/chart/top'

def getImdbTopMovies():
  response = requests.get(URL)

  soup = BeautifulSoup(response.text, 'html.parser')
  #soup = BeautifulSoup(response.text, 'lxml') # faster

  # print(soup.prettify())

  movietags = soup.select('td.titleColumn')
  inner_movietags = soup.select('td.titleColumn a')
  ratingtags = soup.select('td.posterColumn span[name=ir]')

  def get_year(movie_tag):
    moviesplit = movie_tag.text.split()
    year = moviesplit[-1] # last item 
    return year

  years = [get_year(tag) for tag in movietags]
  actors_list =[tag['title'] for tag in inner_movietags] # access attribute 'title'
  titles = [tag.text for tag in inner_movietags]
  ratings = [float(tag['data-value']) for tag in ratingtags] # access attribute 'data-value'

  return (years, actors_list, titles, ratings)