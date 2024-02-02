import requests
from bs4 import BeautifulSoup as BS


def find_category(categories: list, keyword: str) -> list:
    result = []

    for category in categories:
        if keyword.lower() in category.lower():
            result.append(category)
    
    return result


category_list = []

URL = "https://enter.kg/"
response = requests.get(URL)
soup = BS(response.text, "html.parser")

categories = soup.find_all("li", {"class": "VmClose"})

for category in categories:
    title = category.find("a").text
    category_list.append(title)

categories = soup.find_all("span", {"class": "category-product-count"})

for category in categories:
    title = category.text.strip()
    category_list.append(title)

print(find_category(category_list, "Ноутбуки"))
