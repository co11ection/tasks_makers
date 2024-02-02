import json


def create_new(id: int, title: str, description: str, price: int, rating: float) -> None:
    with open("db.json", "r") as db:
        products = json.load(db)
    
    products.append({"id": id, "title": title, "description": description, "price": price, "rating": rating})

    json_result = json.dumps(products)
    
    with open("new_db.json", "w") as db:
        db.write(json_result)
