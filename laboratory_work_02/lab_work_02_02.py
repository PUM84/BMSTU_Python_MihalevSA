x = float(input("Введите значение для переменной X: "))
y = float(input("Введите значение для переменной Y: "))
R = float(input("Введите значение для радиуса R: "))

if y <= R and 0 <= x <= R:
    print ("Внутри")
elif y >= R and 0 >= x >=R:
    print ("Внутри")
elif x**2 + y**2 >= R**2 and 0 <= x <= R and 0 >= y >= -R:
    print ("Внутри")
elif x**2 + y**2 >= R**2 and -R <= x <= 0 and 0 <= y >= R:
    print ("Внутри")
else:
    print ("Снаружи")