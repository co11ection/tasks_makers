class CustomError(Exception):
    pass


capitals_error = CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")


def check_letters(string: str) -> str:
    if not string.isupper():
        raise capitals_error
    
    return f"ВСЕ ОТЛИЧНО! {string}"


print(check_letters("HELLO"))
