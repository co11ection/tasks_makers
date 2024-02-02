def calc_price(filename: str) -> int:
    result = 0

    with open(filename, "r") as file_:
        for line in file_.readlines():
            specs = line.split()
            quantity = float(specs[1])
            price = float(specs[2])
            result += quantity * price
    
    return result
