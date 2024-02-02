def collect_all_possibles(list_: list, num: int) -> list:
    result = []

    for element in list_:
        try:
            result.append(element + num)
        except TypeError:
            pass

        try:
            result.append(element * num)
        except TypeError:
            pass

        try:
            result.append(element // num)
        except TypeError:
            pass

        try:
            result.append(element - num)
        except TypeError:
            pass

        try:
            result.append(element ** num)
        except TypeError:
            pass
        
    return result
