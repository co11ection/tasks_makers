def func12(strings: list, register: str) -> list:
    result = []

    for string in strings:
        modified_string = getattr(string, register)()
        result.append(modified_string)

    return result
