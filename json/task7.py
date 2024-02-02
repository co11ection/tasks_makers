import json


with open("db.json", "r") as db:
    products = json.load(db)

result = []

for product in products:
    product.update({"description": "..."})
    result.append(product)

json_result = json.dumps(result)

with open("new_db.json", "w") as db:
    db.write(json_result)
