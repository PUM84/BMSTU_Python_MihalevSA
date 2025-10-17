from math import sqrt, sin, pi

print('Введите Xbeg, Xend и Dx')

xb = float(input('Xbeg = '))
xe = float(input('Xend = '))
dx = float(input('Dx = '))
print("Xbeg = {0: 7.2f} Xend = {1: 7.2f}"
      .format(xb, xe))
print("  Dx = {0: 7.2f}".format(dx))
xt = xb
print("+--------+--------+")
print("I   X    I    Y   I")
print("+--------+--------+")
while xt <= xe:
    if -9 <= xt <= -5:
        y = -sqrt(4 - (xt + 7) ** 2) + 2
    elif -5 <= xt <= -4:
        y = 2
    elif -4 <= xt <= 0:
        y = -xt / 2
    elif 0 <= xt <= pi:
        y = sin(xt)
    elif pi <= xt:
        y = xt - pi
    print("I{0: 7.2f} I{1: 7.2f} I"
          .format(xt, y))
    xt += dx
print("+--------+--------+")