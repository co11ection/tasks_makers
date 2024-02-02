class Planet:

    def __init__(self, orbit: int) -> None:
        self.orbit = orbit


class Mercury(Planet):

    def __init__(self, orbit: int) -> None:
        super().__init__(orbit)


    def get_age(self, earth_age: int) -> str:
        self.age = earth_age * 365 // self.orbit
        return f"на Меркурии ваш возраст составляет {self.age} лет"


class Venus(Planet):

    def __init__(self, orbit: int) -> None:
        super().__init__(orbit)


    def get_age(self, earth_age: int) -> str:
        self.age = round(earth_age * 365 / self.orbit * 365)
        return f"на Венере ваш возраст составляет {self.age} дней"


class Jupiter(Planet):

    def __init__(self, orbit: int) -> None:
        super().__init__(orbit)


    def get_age(self, earth_age):
        self.age = earth_age * 365 // self.orbit * 365 * 24
        return f"на Юпитере ваш возраст составляет {self.age} часов"


venus = Venus(12)
jupiter = Jupiter(88)
mercury = Mercury(225)

print(venus.get_age(17))
print(jupiter.get_age(23))
print(mercury.get_age(32))
