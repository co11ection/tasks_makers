class RadioMixin:

    def play_music(self, title: str) -> None:
        print(f"Песня называется {title}")


class Auto(RadioMixin):
    pass


class Boat(RadioMixin):
    pass


class Amphibian(Auto, Boat):
    pass


auto = Auto()
boat = Boat()
obj = Amphibian()

auto.play_music("Happy")
boat.play_music("Happy")
obj.play_music("Happy")
