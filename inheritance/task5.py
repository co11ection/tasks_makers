class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


    def display(self) -> None:
        print(f"name:{self.name}, age:{self.age}")


class Student(Person):
    
    def __init__(self, name: str, age: int, faculty: str) -> None:
        super().__init__(name, age)
        self.faculty = faculty
    

    def display_student(self) -> None:
        print(f"name:{self.name}, age:{self.age}, faculty:{self.faculty}")


obj_student = Student("Rick", 21, "science")

obj_student.display()
obj_student.display_student()
