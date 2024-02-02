warehouse = [
    ['1', '2', '3'],
    [1, 2],
    [[1], [2], [3]],
    [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
]

if len(warehouse) > 10:
    raise ValueError
    
for box in warehouse:
    if len(box) > 3:
        raise ValueError
