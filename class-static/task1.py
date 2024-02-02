class Product:
    base_price = 20000


    def __init__(self, model: str, year: int, color: str) -> None:
        self.model = model
        self.year = year
        self.color = color


    def has_garantiya(self, year: int) -> str:
        past_years = year - self.year
        
        if past_years > 2:
            return "Ваша гарантия истекла"

        return "Гарантия действительна"


    @classmethod
    def change_price(cls, rate: float) -> None:
        inflation = round(cls.base_price * (rate / 100))
        cls.base_price += inflation


obj = Product("A218", 2008, "red")

obj.change_price(2)
print(obj.has_garantiya(2010))
print(obj.base_price)
