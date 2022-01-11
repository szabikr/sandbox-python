import random
from algo.get_imdb_top_movies import getImdbTopMovies

# crawl IMDB Top 250 and randomly select a movie

def main():
  years, actors_list, titles, ratings = getImdbTopMovies()
  n_movies = len(titles)

  while(True):
    idx = random.randrange(0, n_movies)
    
    print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

    user_input = input('Do you want another movie (y/[n])? ')
    if user_input != 'y':
      break
    

if __name__ == '__main__':
  main()
