def func15(users: list) -> str:
    result = ""

    for user in users:
        if user["work"].startswith("IT"):
            result += "%s, скидки в магазине компьютерной техники!\n" % user["name"]
    
    return result


users = [
  {"name": "Jack", "age": 35, "work": "IT-backend developer"},
  {"name": "Helen", "age": 35, "work": "Nurse"},
  {"name": "Bob", "age": 35, "work": "Driver"},
  {"name": "Jessica", "age": 35, "work": "IT-frontend developer"},
  {"name": "Helga", "age": 35, "work": "IT-HR"}
]
