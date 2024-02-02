import json


with open("db.json", "r") as db:
    products = json.load(db)
    print(products)

for product in products:
    if product["id"] == 3:
        products.remove(product)
        break

json_result = json.dumps(products)

with open("new_db.json", "w") as db:
    db.write(json_result)
