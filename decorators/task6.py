def is_admin(func):
    def wrapper(*args, **kwargs):
        user = args[0]

        if user["is_admin"]:
            print(f"Доступ разрешен {user['username']}")
        else:
            print(f"Доступ запрещен {user['username']}")

    return wrapper


@is_admin
def get_user(user: dict) -> dict:
    return user


get_user({"username": "john133", "is_admin": True})
get_user({"username": "jane133", "is_admin": False})
