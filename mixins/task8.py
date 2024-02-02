class WalkMixin:

    def walk(self) -> None:
        print("я могу ходить")


class FlyMixin:

    def fly(self) -> None:
        print("я могу летать")


class SwimMixin:

    def swim(self) -> None:
        print("я могу плавать")


class Human(WalkMixin, SwimMixin):
    pass


class Fish(SwimMixin):
    pass


class Exocoetidae(FlyMixin, SwimMixin):
    pass


class Duck(WalkMixin, FlyMixin, SwimMixin):
    pass
