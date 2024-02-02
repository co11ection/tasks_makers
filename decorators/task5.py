def validate_password(func):
    def wrapper(*args, **kwargs):
        username = args[0]
        password = args[1]

        if username not in users:
            print("Username is not defined")
            return
        
        if users[username] != password:
            print("Password is invalid")
            return
        
        func(username, password)
    
    return wrapper


@validate_password
def login(username: str, password: str) -> None:
    print(f"Welcome, {username}")


users = {
    "chrome": "658093",
    "firefox": "3183308",
    "safari": "543481",
}


login("edge", "3663")
