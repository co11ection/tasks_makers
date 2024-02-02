class Game:
    __level = 0


    def __init__(self, name: str) -> None:
        self.name = name
    

    def play(self, hours: int) -> None:
        if hours > 2:
            self.__level += 1


    def get_level(self) -> int:
        return self.__level


game = Game("John")

print(game.get_level())
game.play(3)
game.play(8)
print(game.get_level())
