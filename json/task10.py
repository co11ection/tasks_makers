import json


def get_sorted(json_filename: str) -> list:
    with open(json_filename, "r") as db:
        products = json.load(db)
    
    products.sort(key=lambda product: product["rating"], reverse=True)

    return products
