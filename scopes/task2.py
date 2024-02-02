x = "Я глобальная переменная!"


def my_func() -> str:
    global x

    x = "Я могу изменяться"

    return x


print(x)
print(my_func())
