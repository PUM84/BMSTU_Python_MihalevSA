print('Введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg = '))
xe = float(input('Xend = '))
dx = float(input('Dx = '))
eps = float(input('Eps = '))

print("+--------+-----------+-----+")
print("I   X    I     Y     I  N  I")
print("+--------+-----------+-----+")

xt = xb
while xt <= xe:
    an = 1.0
    n = 0
    y = an

    while True:
        n += 1
        an = an * xt / n
        y += an

        if abs(an) < eps:
            break

    print("I{0: 7.3f} I{1: 9.3f} I{2: 3} I".format(xt, y, n))
    xt += dx

print("+--------+-----------+-----+")