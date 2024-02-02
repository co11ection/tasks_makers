balance = 0


def get_salary(amount: int) -> None:
    global balance

    balance +=amount


def pay_bills(amount: int, log_name: str) -> None:
    global balance

    balance -= amount
    
    print(f"Вы заплатили {amount} сом за {log_name}")


def get_balance() -> None:
    print(f"У вас на счету {balance} сом")


get_salary(1000)
get_balance()
pay_bills(400, 'кабельное тв')
get_balance()
