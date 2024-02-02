dict_ = {
    "Sasha": {
        "likes": 23,
        "comments": 2,
        "rating": 4
    },
    "Aliya": {
        "likes": 34,
        "comments": 5,
        "rating": 5
    },
    "Dasha": {
        "likes": 15,
        "comments": 3,
        "rating": 2
    },
    "Luna": {
        "likes": 12,
        "comments": 2,
        "rating": 1
    },
    "Rena": {
        "likes": 26,
        "comments": 7,
        "rating": 2
    }
}

print(sum([value for element in dict_.values() for key, value in element.items() if element["rating"] > 3 and key == "likes"]))
