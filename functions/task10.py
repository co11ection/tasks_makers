def sum_digits(number: int) -> int:
    result = 0

    for digit in str(number):
        result += int(digit)
    
    return result
