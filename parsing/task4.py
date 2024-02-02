import requests
from bs4 import BeautifulSoup as BS


def getTitle(url: str) -> str:
    response = requests.get(url)
    soup = BS(response.text, "html.parser")

    h1 = soup.find("h1")

    return h1 if h1 else "Title could not be found"


print(getTitle('http://www.example.com/'))
