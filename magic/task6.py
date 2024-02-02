class Kopilka:

    def __init__(self) -> None:
        self.__total = 0
        self.__coins = []


    def add_moneta(self, moneta: int) -> None:
        self.__coins.append(moneta)
        self.__total += moneta


    def __len__(self) -> int:
        return len(self.__coins)


    def __getitem__(self, index: int) -> int:
        return self.__coins[index]


obj = Kopilka()

obj.add_moneta(25)
obj.add_moneta(30)
print(len(obj))

for i in obj:
    print(i)
