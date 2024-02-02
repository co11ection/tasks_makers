class Money:

    def __init__(self, country: str, symbol: str) -> None:
        self.country = country
        self.symbol = symbol


class Dollar(Money):
    rate = 84.8


    def exchange(self, amount: float) -> str:
        som = amount * self.rate
        return f"$ {amount} равен {som} сомам"


class Euro(Money):
    rate = 98.4


    def exchange(self, amount: float) -> str:
        som = amount * self.rate
        return f"€ {amount} равен {som} сомам"
