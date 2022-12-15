from bs4 import BeautifulSoup
import requests
from operator import itemgetter


data = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies"
                    "-2/")
data = data.text

soup = BeautifulSoup(data, "html.parser")

movies = soup.find_all("h3", class_="title")

try:
    with open("movies.txt", "w") as movie_data:
        for movie in reversed(movies):
            each_movie = movie.getText().split(" ", 1)
            movie_data.write(f"{each_movie[0]} {each_movie[1]}\n")
except FileExistsError:
    with open("movies.txt", "a") as movie_data:
        each_movie = movie.getText().split(" ", 1)
        movie_data.write(f"{each_movie[0]} {each_movie[1]}\n")

# or use slice operator - list[::-1] also r