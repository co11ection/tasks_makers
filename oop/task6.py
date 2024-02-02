class Salary:
    percent = 8


    def __init__(self, salary: float, experience: int) -> None:
        self.salary = salary
        self.experience = experience


    def count_percent(self) -> float:
        month_tax = self.salary / 100 * self.percent
        result = self.experience * month_tax
        return result


obj = Salary(10000, 10)
print(obj.count_percent())
