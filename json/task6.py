import json


json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'

products = json.loads(json_products)

for product in products:
    if product["rating"] > 4:
        print(product["title"])
