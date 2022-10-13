# 1. append() - добавляет элемент в конец списка
# data = [12, 432, 324234, 44]
# data.append(456)
# print(data)

#clear() - удаляет все элементы из списка //remove() - удаляет выбранный элимент
# my_list = [12, 'usa', 'sun', 14, 'mars']
# my_list.clear()
# my_list.remove(12)
# print(my_list)

#copy() - делает поверхностную копию списка
# import copy
# result_A = [90, 85, 82]
# result_B = copy.deepcopy(result_A)
# print(result_A)
# print(result_B)

#count() - считает сколько раз в списке встречается переданный аргумент

str = 'этот строковый пример.....!!!!!'
sub = '.'
print("str.count('.') :", str.count(sub))
sub = 'прим'
print("str.count('прим', 10, 30) : ", str.count(sub, 10, 30))