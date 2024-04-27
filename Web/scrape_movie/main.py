from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(url=URL)
emp_web_pag = r.text

# h3 class_=title
soup = BeautifulSoup(emp_web_pag, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movies_list = []

for movies in all_movies:
    movie = movies.getText()
    movies_list.insert(0, movie)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for m in movies_list:
        file.write(f"{m}\n")