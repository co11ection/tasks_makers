class Taxi:
    
    def __init__(self, name: str, cost: float, cost_km: float) -> None:
        self.name = name
        self.cost = cost
        self.cost_km = cost_km
    

    def get_total_cost(self, km: float) -> str:
        total_cost = self.cost + km * self.cost_km
        info = f"Такси {self.name}, стоимость поездки: {total_cost} сом"
        return info


taxi1 = Taxi("Namba", 19, 16)
taxi2 = Taxi("Yandex", 37, 15)
taxi3 = Taxi("Jorgo", 0, 17)

print(taxi1.get_total_cost(10)) 
print(taxi2.get_total_cost(6)) 
print(taxi3.get_total_cost(14))  
