# Найдите три ключа с самыми высокими значениями в словаре
#  my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

from audioop import reverse


my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 6000}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:7]

print(result )


result2 = sorted(my_dict.values(), reverse = True)[:7]

print(result2 )

