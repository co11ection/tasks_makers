def func20(products: list, title: str) -> list:
    filtered_data = [product for product in products if title.lower() in product.get("title").lower()]
    
    return filtered_data
