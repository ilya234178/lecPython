# colors = ['red' , 'green' , 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors)    # разделителей не будет
# data.write('\nLINE 2 \n')
# data.write('LINE 3 \n')
# data.close()

# with open('file.txt' , 'w') as data:
#     data.write('\nLine 1 \n')
#     data.write('Line 2 \n')
                                           #a - дописывает данные в файл
                                           #w - переписывает данные из файла
                                           # r - считывает данные из файла


# path = 'file.txt'
# data = open(path , 'r')
# for line in data:
#     print(line)
# data.close()

# import hello as h         # перенос функции из другого файла
# print(h.f(1))

# def new_string(symbol , count = 3):
#     return symbol * count

# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res +=item
#     return res

# print(concatenatio('a','s','d','w'))
# print(concatenatio('a','1'))

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# list = []
# for e in range (1,10):
#     list.append(fib(e))
# print(list)

# a = (3, 4, 5)                   #кортежи - неизменяемый список
# print(a)
# print(a[0])
# for item in a:
#     print(item)



