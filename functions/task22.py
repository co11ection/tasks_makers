balance = 0.0


def spent(target: str, spend: float, balance: float) -> tuple:
    spend = int(spend)

    if balance > spend:
        balance -= spend
        data = {"target" : target, "spend" : spend}

        return data, balance
    else:
        return "Недостаточно средств"


def deposit(sum_: float, balance: float) -> float:
    balance = balance+sum_

    return balance


print(deposit(100, balance))
print(spent("milk", 120, balance))
