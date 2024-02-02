def type_check(correct_type):
    def wrapper(func):
        def wrapper2(*args, **kwargs):
            if type(args[0]) == correct_type:
                func(*args)
            else:
                print("Неверный тип данных :(")

        return wrapper2

    return wrapper


@type_check(int)
def func1(num: int) -> None:
    print(num*2)


func1(2)
func1({1: "какой-то", 2: "словарь"})
