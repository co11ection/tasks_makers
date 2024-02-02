def bad_students(filename: str) -> list:
    result = []

    with open(filename, "r") as file_:
        for line in file_.readlines():
            student = line.split()
            grade = student[2]

            if int(grade) < 4:
                surname = student[1]
                result.append(surname)

    return result
