def func13(string: str) -> dict:
    result = {}

    for symbol in string:
        result.update({symbol: string.count(symbol)})
    
    return result
