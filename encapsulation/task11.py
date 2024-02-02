class Game:
    __level = 0


    def __init__(self, name: str):
        self.name = self.__validate_name(name)


    def __validate_name(self, name):
        return name.title()


    def set_level(self, upgrade_level):
        if self.name == "Tolik":
            self.__level = upgrade_level
            return self.__level

        print(f"{self.name} ты не Tolik!")


game = Game("Raychel")
print(game._Game__level)
print(game.set_level(5))

game2 = Game("TOLIK")
print(game2._Game__level)
print(game2.set_level(5))
