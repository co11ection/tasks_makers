import json


def bulk_create(products: list) -> None:
    with open("db.json", "r") as db:
        source_products = json.load(db)

    ids = []

    for product in source_products:
        ids.append(product["id"])

    for product in products:
        if product["id"] in ids:
            products.remove(product)

    # source_products.extend(products)
    json_result = json.dumps(source_products)

    with open("new_db.json", "w") as db:
        db.write(json_result)
