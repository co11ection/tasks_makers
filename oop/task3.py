class BankAccount:

    def __init__(self) -> None:
        self.balance = 0


    def withdraw(self, amount: float) -> None:
        self.balance -= amount
        info = f"Ваш баланс: {self.balance} сом"
        print(info)


    def deposit(self, amount: float) -> None:
        self.balance += amount
        info = f"Ваш баланс: {self.balance} сом"
        print(info)


account = BankAccount()
account.deposit(1000)
account.withdraw(500)
