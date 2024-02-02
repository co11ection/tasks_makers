class Game:
    __level = 0


    @property
    def level(self) -> int:
        return self.__level


    @level.setter
    def level(self, new_level: int) -> None:
        self.__level = new_level


game = Game()

print(game.level)
game.level = 10
print(game.level)
