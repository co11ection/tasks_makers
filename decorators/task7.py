def route(func):
    def wrapper(*args, **kwargs):
        URL = "https://www.mywebsite.com/"
        uri = args[0]

        return URL + uri

    return wrapper


@route
def get_page(path: str) -> str:
     return path


print(get_page('about/'))
print(get_page('products/'))
