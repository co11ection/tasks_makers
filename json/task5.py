import json


users = [
    {
        'name': 'John',
        'last_name': 'Snow',
        'age': 26,
        'has_car': True,
    },
    {
        'name': 'Sam',
        'last_name': 'Bolt',
        'age': 4,
        'has_car': False,
    }
]


json_users = json.dumps(users)
