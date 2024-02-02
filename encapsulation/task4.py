class Car:
    
    def __init__(self) -> None:
        self.__speed = 0


    @property
    def speed(self) -> int:
        return self.__speed


    @speed.setter
    def speed(self, speed: int) -> None:
        self.__speed = speed


car1 = Car()

print(car1.speed)
car1.speed = 20
print(car1.speed)
