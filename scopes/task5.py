result = 0


def pow_first(x: float, y: float) -> None:
    global result

    result = pow(x,y)


def pow_second(z: float) -> None:
    global result

    result %= z


pow_first(2, 3)
pow_second(3)

print(result)
