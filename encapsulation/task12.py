class Game:
    __level = 0


    def __init__(self, name: str) -> None:
        self.name = name


    def get_level(self) -> int:
        return self.__level


    def set_level(self, new_level: int) -> None:
        self.__level = new_level


game = Game("Chess")

print(game.get_level())
print(game.set_level(10))
