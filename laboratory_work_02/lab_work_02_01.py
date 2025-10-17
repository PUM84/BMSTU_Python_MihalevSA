from math import sqrt, sin, pi

x = float(input("Введите значение X = "))
y = 0.0

if -9 <= x <= -5:
    y = -sqrt(4 - (x+7)**2) + 2
elif -5 <= x <= -4:
    y = 2
elif -4 <= x <= 0:
    y = -x/2
elif 0 <= x <= pi:
    y = sin(x)
elif pi <= x:
    y = x - pi

print("X = {0:.2f} Y = {1:.2f}".format(x, y))