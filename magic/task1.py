class Account:

    def __init__(self, name: str, balance: float, city: str) -> None:
        self.name = name
        self.balance = balance
        self.city = city
        
        print("Счет создан")


    def __repr__(self) -> str:
        return f"{self.name} {self.balance}"


    def __str__(self) -> None:
        return f"Hello {self.name} {self.balance} {self.city}"


    def __del__(self) -> None:
        print("Пока")


obj_account = Account("Rick", 2013, "Bishkek")

print(obj_account)  
print(repr(obj_account)) 
