my_dict = {'a':1, 'b':2, 'c':3}
try:
    value = my_dict['a']
except KeyError:
        print('A KeyError occurred!')  #выдает если ошибка ключа
finally:
        print('The finally statement has executed!')    
        
