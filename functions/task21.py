def func21(products: list, category: str) -> list:
    filtered_data = [product for product in products if product.get("category") == category]

    return filtered_data
