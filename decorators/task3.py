def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func()}</b>"
    
    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func()}</i>"
    
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func()}</u>"
    
    return wrapper


@make_bold
@make_italic
@make_underline
def hello() -> str:
    return "Hello world"
 

print(hello())
