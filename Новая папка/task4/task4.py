# Напишите программу для слияния нескольких словарей в один.

import operator
d1 = {1: 3, 2: 6, 3: 18}
d2 = {4: 11, 5: 23}
d3 = {6: 55, 7: 48}
# result = {}
# for d in (d1, d2, d3):
#     result.update(d)
#     print(result)

result = {**d1, **d2, **d3}
print(result)