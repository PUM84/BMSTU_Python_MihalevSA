from math import *
from random import *

R = float(input("Введите значение для радиуса R: "))

flag = 0
print("    X       Y   Res")
print("-------------------")
for n in range(10):
    x = uniform(-R, R)
    y = uniform(-R, R)

    if ((((y <= R and 0 <= x <= R)
          or (y >= R and 0 >= x >= R))
         or x**2 + y**2 >= R**2 and 0 <= x <= R and 0 >= y >= -R)
        or x**2 + y**2 >= R**2 and -R <= x <= 0 and 0 <= y >= R):
        flag = 1

    else:
        flag = 0

    print("{0: 7.2f} {1: 7.2f}"
          .format(x, y), end=" ")
    if flag:
        print("Yes")
    else:
        print("No")