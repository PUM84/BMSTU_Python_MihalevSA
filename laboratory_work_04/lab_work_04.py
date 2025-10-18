from random import uniform

n = int(input("Элементов в массиве (N<=30) N: "))
if n > 30:
    n = 30
elif n < 5:
    n = 5

print("Начальное состояние")
mas = []
for i in range(n):
    mas.append(uniform(-5, 5))
    print("{0: 2.1f}".format(mas[i]), end=" ")
print()

mult = float(1)
for i in range(n):
    if i % 2 == 0:
        mult *= mas[i]

for i in range(n//2 + 1):
    for j in range(0, n - i - 1):
        if mas[j] > mas[j + 1]:
            mas[j], mas[j + 1] = mas[j + 1], mas[j]

sum = 0
for i in range(1, n-1):
    sum += mas[i]

print("Конечное состояние")
for i in range(n):
    print("{0: 2.1f}".format(mas[i]), end=" ")
print()

print("mult = {0:7.2f} sum = {1:2.1f}".format(mult, sum))