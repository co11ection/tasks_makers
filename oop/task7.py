from datetime import datetime


class Nobel:

    def __init__(self, category: str, year: int, winner: str) -> None:
        self.category = category
        self.year = year
        self.winner = winner


    def get_year(self) -> str:
        current_year = int(datetime.now().strftime("%Y"))
        past_years = current_year - self.year
        info = f"выиграл {past_years} лет назад"
        return info


winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())

winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())
