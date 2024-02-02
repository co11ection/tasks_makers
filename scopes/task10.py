a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]


def lower_7() -> list:
    filtered_data = [num for num in a if num < 7]

    return filtered_data


print(lower_7())
