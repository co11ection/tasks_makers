class Bike:

    def __init__(
        self,
        cost: float, make: str, model: str, year: int, min_profit: float,
        sale_price: float=None, sold: bool=False
    ) -> None:
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self._sale_price = sale_price
        self.sold = sold
        self.min_profit = min_profit


    def set_cost(self, cost: float) -> None:
        if cost < self.cost:
            self._sale_price = cost + self.min_profit
            return

        self._sale_price = cost


    def service(self, price: float) -> float:
        self._sale_price += price
        return self._sale_price


    def sell(self) -> float:
        self.sold = True
        return self.cost - self._sale_price


    @classmethod
    def get_default_bike(cls):
        return cls(10000, "Author", "Basic ASL", 2020, 2000)


bike = Bike.get_default_bike()

bike.set_cost(6000)
bike.service(300)
print(bike.sell())
print(bike.cost)
print(bike.make)
print(bike.year)
print(bike._sale_price)
print(bike.sold)
print(bike.min_profit)
