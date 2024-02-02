def get_full_number(func):
    def wrapper(*args, **kwargs):
        numbers = args[0]
        full_numbers = []
    
        for number in numbers:
            full_numbers.append(f"+996 {number[1:4]} {number[4:]}")
            result = func(full_numbers)

            return result
    
    return wrapper


@get_full_number
def sort_phone_nums(numbers: list) -> str:
    numbers.sort()
    result = "#".join(numbers)
    
    return result


print(sort_phone_nums(["0777987456", "0555123456", "0770369852"]))
