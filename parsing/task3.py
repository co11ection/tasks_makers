import requests
from bs4 import BeautifulSoup as BS


URL = "https://www.wikipedia.org/"
response = requests.get(URL)
soup = BS(response.text, "html.parser")

div = soup.find("div", {"class": "lang5"})
result = div.find("a").text

print(result)
