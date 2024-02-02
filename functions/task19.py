def get_marks(student: dict) -> int:
    return student["marks"]


def func19(students: list) -> list:
    students.sort(key=get_marks, reverse=True)

    return students
