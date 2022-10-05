# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

# Выведите все элементы, которые меньше 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [3, 2, 4, 1]
# for i in a:
#     if i < 5:
#        print(i)

print(list(filter(lambda i: i < 5, b )))    #filter -фильтрует элементы по заданному условию
print(list(filter(lambda i: i < 5, a )))
print()
print([elem for elem in a if elem < 5 ])