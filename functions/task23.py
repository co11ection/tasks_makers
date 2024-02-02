database = []


def create(database: list, title: str, price: float, category: str) -> list:
    data = {
        "title" : title,
        "price" : price,
        "category" : category,
    }
    database.append(data)

    return database


def read(database: list) -> list:
    return database


def update(database: list, index: int, title: str, price: float, category: str) -> list:
    try:
        database[index].update({"title" : title, "price" : price, "category" : category})

        return database
    except:
        return "We dont have this data"


def delete(database: list, index: int) -> list:
    try:
        database.pop(index)

        return database
    except:
        return "We dont have this data"
