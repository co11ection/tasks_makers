import json


with open("task1.json", "r") as file_:
    python_obj = json.load(file_)

with open("task1.py", "w") as file_:
    file_.write(str(python_obj))
