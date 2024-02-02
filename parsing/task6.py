import requests
from bs4 import BeautifulSoup as BS


def get_link(movie_list: list, name: str) -> str:
    for movie in movie_list:
        if name.lower() in movie["title"].lower():
            return movie["link"]


title_list = []

URL = "https://www.imdb.com"
URI = "/chart/top/"
response = requests.get(URL + URI)
soup = BS(response.text, "html.parser")
movies = soup.find_all("td", {"class": "titleColumn"})

for movie in movies:
    tag_a = movie.find("a")
    title = tag_a.text
    uri = tag_a.get("href")
    title_list.append({"title": title, "link": URL + uri})

link = get_link(title_list, "shawshank")
print(link)
