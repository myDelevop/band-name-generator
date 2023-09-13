import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

h3_titles = soup.find_all(name="h3", class_="title")

top_hundred_movies = []

for h3 in h3_titles:
    if h3.text.find(")") == -1:
        split = h3.text.replace(":", ")").split(")")
    else:
        split = h3.text.split(")")
    ranking = int(split[0])
    title = split[1].strip()
    movie = {
        "ranking": ranking,
        "title": title
    }
    top_hundred_movies.append(movie)

top_hundred_movies.reverse()
print(top_hundred_movies)

with open("./top_100_movies.txt", "w", encoding='utf-8') as file:
    for movie in top_hundred_movies:
        file.write(f"{movie['ranking']}) {movie['title']}\n")
