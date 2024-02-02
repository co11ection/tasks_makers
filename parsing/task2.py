import requests
from bs4 import BeautifulSoup as BS


URL = "http://www.example.com/"
response = requests.get(URL)
soup = BS(response.text, "html.parser")

h1 = soup.find("h1").text
paragraph = soup.find("p").text
link = soup.find("a").get("href")

print(f"h1: {h1}\np: {paragraph}\na: {link}")
