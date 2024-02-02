import json


def filter_by_price(price: int) -> list:
    with open("db.json", "r") as db:
        products = json.load(db)

    result = [product for product in products if product["price"] >= price]

    return result
