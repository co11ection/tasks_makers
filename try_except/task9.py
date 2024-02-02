try:
    cash = int(input())
    if cash < 0:
        raise ValueError("Сумма не может быть отрицательной!")
except ValueError as error:
    print(error)
else:
    print(cash)
