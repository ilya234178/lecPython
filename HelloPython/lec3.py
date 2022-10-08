# def f(x):
#     x**2


# g = f
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# def calc1(x):
#     return x+10
#  print(calc1(10))

# def calc2(x):
#     return x*10
#  print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y +1

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#      return op(a, b)

# calc(lambda x, y: x+y +1, 4, 5)


# list = []

# for i in range(1, 101):
#     # if(i%2 == 0):
#         list.append(i)

# print(list)
# list = [i for i in range(1, 21) if i% 2 == 0]
# list = [(i, i) for i in range(1, 21) if i% 2 == 0]


# def f(x):
#     return x**3
# list = [(i,f(i)) for i in range(1, 21) if i% 2 == 0]
# print(list)

# path = '/Users/natalasamofal/Desktop/python/Dz_Python/file.txt'
# f = open(path, 'r')
# data = f.read()+ ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)


# def select(f, col):
#   return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f (x)]

# data = '1 2 3 4 5 8 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# li = [x for x in range(1,21)]

# li = list(map(lambda x:x+10, li))

# print(li)

# data = list(map(int, input().split()))
# print (data)


# data = list(map(int, input().split()))
# for e in data:
#     print(e)

# print('--')
# for e in data:
#     print(e)


# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)


users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(enumerate(users))
print(data)