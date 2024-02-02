def read_last(lines: int, filename: str) -> None:
    with open(filename, "r") as file_:
        lines_list = file_.readlines()

    if lines >= len(lines_list):
        lines_list.reverse()

        for line in lines_list:
            print(line.strip("\n"))
    else:
        indexes = list(range(len(lines_list)-lines, len(lines_list)))
        indexes.reverse()

        for ind in indexes:
            print(lines_list[ind].strip("\n"))
