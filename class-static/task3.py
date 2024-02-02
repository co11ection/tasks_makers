class Makers:
    student_count = 0


    def __init__(self, name: str, language: str, kpi: float) -> None:
        self.name = name
        self.language = language
        self.kpi = kpi


    @classmethod
    def new_student(cls, name: str, language: str, kpi: float):
        cls.student_count += 1
        student = cls(name, language, kpi)
        return student


    def get_info(self) -> str:
        return f"Student name: {self.name}, Language: {self.language}"


    def set_kpi(self, kpi: float) -> float:
        self.kpi = kpi
        return self.kpi


student1 = Makers.new_student("Vlad", "Python", 0)
student2 = Makers.new_student("Malik", "JavaScript", 0)

print(student1.set_kpi(89))
print(student1.get_info())
print(student2.set_kpi(89))
print(student2.get_info())
print(Makers.student_count)
