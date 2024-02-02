import requests
from time import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        func()
        end = time()
        time_exec = end - start
        
        print(f"Время выполнения: {time_exec} секунд.")
    
    return wrapper


@benchmark 
def fetch_webpage() -> None: 
    webpage = requests.get('https://google.com')


fetch_webpage()
