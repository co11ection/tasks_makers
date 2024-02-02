import json


with open('task2.json') as file_:
    json_obj = file_.read()

python_obj = json.loads(json_obj)
