from datetime import datetime


def func_start_time(func):
    def wrapper(*args, **kwargs):
        print(f"Функция запущена {datetime.now()}")
        func()
    
    return wrapper
        

@func_start_time
def func() -> None:
    print("Hello world")


func()
