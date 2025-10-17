x = float(input("Введите значение для переменной X: "))
y = float(input("Введите значение для переменной Y: "))
R = float(input("Введите значение для радиуса R: "))

result = "Снаружи"

if (y <= R and 0 <= x <= R) or \
   (y >= R and 0 >= x >= R) or \
   (x**2 + y**2 >= R**2 and 0 <= x <= R and 0 >= y >= -R) or \
   (x**2 + y**2 >= R**2 and -R <= x <= 0 and 0 <= y >= R):
    result = "Внутри"

print(result)