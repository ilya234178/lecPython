program = 'Путевой компьютер'
stars = 80        #количество звездочек
tabs = 4          #количество отступов

dist = 0           #расстояние , которое нужно проехать
speed = 0          #средняя скорость авто 
time = 0           #время движения (за рулем)
total_time = 0     #общее количество времени в пути
drive_hours = 0    #часов в движении полных 
drive_mins = 0     #минут( остаток)
total_hours = 0    #часов всего(полных)
total_min = 0      #минут всего

tank = 0           #размер бака
consum = 0         #средний расход л/100км
dist = 0           #расстояние в км
refuels = 0        #количество дозаправок
refuel_time = 20   #время дозаправки
fuel = 0           #сколько затрачено топлива
price = 0          #цена
breaks = 0         #количество плановых остановок 
break_time = 0     #время каждой плановой остановки

#выводим заголовок
print('\t' * tabs , program)
print('*' * stars)

#ввод данных от пользователя
dist = int(input('Введите расстояние, км: '))
speed = int(input('Планируемая скорость: '))
consum = float(input('Введите средни расход топлива(л/100км): '))
tank = float(input('Объем бака: '))
price = float(input('Стоимость 1 литра топлива:  '))
breaks = float(input('Количество плановых остановок: '))
break_time = float(input('Время плановой остановки , мин: '))

#производим вычисления
time = dist * 60 / speed          #время за рулем
fuel = consum * dist / 100        #всего затрачено топлива

refuels = fuel // tank
total_time = time + refuels * refuel_time + breaks * break_time

drive_hours = time // 60
drive_mins = time - drive_hours * 60

total_hours = total_time // 60
total_mins = total_time - total_hours * 60


print('*' * stars)
print('\t' * tabs , 'Результаты: ')

print('Время за рулем: ', int(drive_hours), 'ч.', int(drive_mins), 'м.')
print('Общее время пути: ', int(total_hours), 'ч.', int(total_mins), 'м.')
print('Количество дозаправок: ', refuels)
print('Потрачено времени на дозаправку: ',  refuels * refuel_time, 'минут')
print('Израсходовано топлива: ', fuel)
print('Стоимость топлива: ', fuel * price)