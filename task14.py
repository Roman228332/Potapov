print ('Введите x точки:')
a = int(input())
print ('Введите y точки:')
b = int(input())
print ('Координаты вашей точки: (', a, ';', b, ')')
if a >= 0 and a <= 5 and b >= 0 and b <= 5:
    print('Ваша точка принадлежит квадрату')
else:
    print('Ваша точка не принадлежит квадрату')