class Person:

    def __init__(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name
    

    def get_info(self) -> str:
        return f"Привет, меня зовут {self.name} {self.last_name}"


class Employee(Person):

    def __init__(self, name: str, last_name: str, work: str, status: str) -> None:
        super().__init__(name, last_name)
        self.work = work
        self.status = status


    def get_info(self) -> str:
        return f"Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}"


class Student(Person):

    def __init__(self, name: str, last_name: str, university: str, course: int) -> None:
        super().__init__(name, last_name)
        self.university = university
        self.course = course
        

    def get_info(self) -> str:
        return f"Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе"


def get_human_info(human) -> None:
    print(human.get_info())


employee = Employee("Иван", "Петров", "Рога и копыта", "директор")
student = Student("Иван", "Петров", "КГТУ", 3)
person = Person("Иван", "Петров")

get_human_info(employee)
get_human_info(student)
get_human_info(person)
