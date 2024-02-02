import json


def update(id: int, title: str=None, price: int=None, rating: float=None) -> None:
    with open("db.json", "r") as db:
        products = json.load(db)
    
    for product in products:
        if product["id"] == id:
            if title:
                product.update({"title": title})
            if price:
                product.update({"price": price})
            if rating:
                product.update({"rating": rating})
            break
    else:
        raise ValueError
    
    json_result = json.dumps(products)
    
    with open("new_db.json", "w") as db:
        db.write(json_result)
