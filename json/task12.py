import json


def search(name: str) -> list:
    with open("db.json", "r") as db:
        products = json.load(db)

    result = [product for product in products if name in product["title"]]

    return result
