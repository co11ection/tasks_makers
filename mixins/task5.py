class Square:

    def __init__(self, side: float) -> None:
        self.side = side


    def get_area(self) -> float:
        area = self.side**2
        return area


class Triangle:

    def __init__(self, height: float, base: float) -> None:
        self.height = height
        self.base = base


    def get_area(self) -> float:
        area = self.base / 2 * self.height
        return area


class Pyramid(Triangle, Square):

    def __init__(self, height: float, base: float) -> None:
        super().__init__(height, base)


    def get_volume(self) -> int:
        volume = int(1/3 * self.base**2 * self.height)        
        return volume
