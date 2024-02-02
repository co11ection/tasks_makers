list_ = [1,2,3,4,5,6,7,8,9,0]
step = 2
dynamic_step = step
element = 'A'
amount = len(list_) // step

for _ in range(amount):
    list_.insert(dynamic_step, element)
    dynamic_step += step + 1

print(list_)
