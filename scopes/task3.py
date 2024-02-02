num = 3


def mul() -> int:
    global num

    num = num**2
    
    return num


mul()
mul()
mul()

print(num)
