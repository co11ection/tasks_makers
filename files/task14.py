def reverse_file_print(filename: str) -> None:
    with open(filename, "r") as file_:
        for line in file_.readlines():
            print(line[::-1])
