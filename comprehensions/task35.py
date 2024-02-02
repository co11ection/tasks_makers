dict_ = {
    "Dasha": {
        "likes": 15,
        "comments": [
            {"id": 1, "text": "some text"},
            {"id": 2, "text": "some text"},
        ],
        "rating": 2
    },
    "Luna": {
        "likes": 12,
        "comments": [
            {"id": 1, "text": "some text"},
            {"id": 2, "text": "some text"},
            {"id": 3, "text": "some text"},
        ],
        "rating": 1
    },
    "Rena": {
        "likes": 26,
        "comments": [
            {"id": 1, "text": "some text"},
            {"id": 2, "text": "some text"},
            {"id": 3, "text": "some text"},
            {"id": 4, "text": "some text"},
            {"id": 5, "text": "some text"},
            {"id": 6, "text": "some text"},
        ],
        "rating": 2
    }
}

result = [comment["id"] for element in dict_.values() for key, value in element.items() if key == "comments" for comment in value if len(value) > 3]
 
print(result)
