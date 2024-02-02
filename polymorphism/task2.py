class Dog:
    
    def voice(self) -> None:
        print("Гав")


class Cat:

    def voice(self) -> None:
        print("Мяу")


def to_pet(animal) -> None:
    animal.voice()


barsik = Cat()
rex = Dog()

to_pet(barsik)
to_pet(rex)
