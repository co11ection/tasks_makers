import requests


URL = "https://stackoverflow.com/questions/"
source = requests.get(URL).status_code

print(source)
