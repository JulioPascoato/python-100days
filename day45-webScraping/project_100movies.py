import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movies = [movie.getText() for movie in soup.select("h3", class_="title")]
movies.reverse()

with open("movies.txt", "a") as file:
    for movie in movies:
        file.write(f"{movie}\n")


