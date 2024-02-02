def read_csv(filename: str) -> dict:
    result = {}

    with open(filename, "r") as file_:
        for line in file_.readlines():
            elements = line.strip().split(",")
            result.update({elements[0]: elements[1:]})
    
    return result
