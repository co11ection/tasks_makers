class MoneyFmt:

    def __init__(self, amount: float) -> None:
        self.amount = amount


    def update(self, amount: float) -> None:
        self.amount = amount
    

    def __repr__(self) -> str:
        return str(self.amount)


    @staticmethod
    def dollarize(float_num: float) -> str:
        return f"${float_num:,.2f}".replace("$-", "-$")


    def __str__(self) -> str:
        return MoneyFmt.dollarize(self.amount)
    

cash = MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
print(repr(cash))
