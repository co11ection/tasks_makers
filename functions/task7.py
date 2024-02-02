def is_palindrome(string: str) -> bool:
    string = string.lower()

    return string == string[::-1]
