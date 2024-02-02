class Student:

    def __init__(self, name: str, class_name: str, ball: dict) -> None:
        self.name = name
        self.class_name = class_name
        self.ball = ball


    def get_average(self, other) -> tuple:
        self_grades = self.ball.values()
        other_grades = other.ball.values()
        self_average = sum(self_grades) / len(self_grades)
        other_average = sum(other_grades) / len(other_grades)

        return self_average, other_average


    def __gt__(self, other) -> bool:
        averages = self.get_average(other)
        result = f"> {averages[0] > averages[1]}"
        return result


    def __lt__(self, other) -> bool:
        averages = self.get_average(other)
        result = f"< {averages[0] < averages[1]}"
        return result

    def __ge__(self, other) -> bool:
        averages = self.get_average(other)
        result = f">= {averages[0] >= averages[1]}"
        return result


    def __le__(self, other) -> bool:
        averages = self.get_average(other)
        result = f"<= {averages[0] <= averages[1]}"
        return result


obj_student1 = Student("a", "A", {"math": 100, "history": 50, "literature": 88})  
obj_student2 = Student("b", "Aa", {"math": 100, "history": 50, "literature": 88})  

print(obj_student1 > obj_student2)
print(obj_student1 < obj_student2)
print(obj_student1 >= obj_student2)
print(obj_student1 <= obj_student2)
