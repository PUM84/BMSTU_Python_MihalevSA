from math import *

x = float(input('Введите параметр x: '))
y1 = (sin(2*x)+sin(5*x)-sin(3*x))/(cos(x)+1-2*sin(2*x)**2)
y2 = 2*sin(x)
print('Результат программы для уравнения 1:', y1)
print('Результат программы для уравнения 2:', y2)