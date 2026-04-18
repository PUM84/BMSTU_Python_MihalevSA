"""Модуль с функциями из лабораторных работ 1, 4 и 5."""

__all__ = ['hello', 'calc_expression', 'process_array', 'process_matrix']
VERSION = '1.0.0'

def hello():
    """Вывод приветствия."""
    print("Hello Python!")

def calc_expression(x):
    """Вычисление двух тригонометрических выражений."""
    from math import sin, cos
    y1 = (sin(2*x) + sin(5*x) - sin(3*x)) / (cos(x) + 1 - 2*sin(2*x)**2)
    y2 = 2 * sin(x)
    return y1, y2

def process_array(n=None):
    """
    Генерация массива, вычисление произведения элементов с чётными индексами,
    сортировка и сумма внутренних элементов.
    """
    from random import uniform

    if n is None:
        n = int(input("Элементов в массиве (N<=30) N: "))
    if n > 30:
        n = 30
    elif n < 5:
        n = 5

    mas = [uniform(-5, 5) for _ in range(n)]
    mult = 1.0
    for i in range(n):
        if i % 2 == 0:
            mult *= mas[i]

    for i in range(n // 2 + 1):
        for j in range(0, n - i - 1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]

    total = sum(mas[1:-1])
    return mas, mult, total

# ---------- ЛР5 ----------
def process_matrix(n=None):
    """
    Создание квадратной матрицы случайных чисел.
    Определение количества столбцов с нулём и номера строки с самой длинной серией.
    """
    from random import randint

    if n is None:
        n = int(input("Введите размер квадратной матрицы (N): "))

    A = [[randint(0, 9) for _ in range(n)] for _ in range(n)]

    count_cols_with_zero = sum(
        any(A[row][col] == 0 for row in range(n)) for col in range(n)
    )

    max_series_length = 0
    row_with_max_series = -1
    for i, row in enumerate(A):
        current_length = 1
        max_length_in_row = 1
        for j in range(1, n):
            if row[j] == row[j - 1]:
                current_length += 1
            else:
                if current_length > max_length_in_row:
                    max_length_in_row = current_length
                current_length = 1
        if current_length > max_length_in_row:
            max_length_in_row = current_length
        if max_length_in_row > max_series_length:
            max_series_length = max_length_in_row
            row_with_max_series = i

    return A, count_cols_with_zero, row_with_max_series + 1

if __name__ == '__main__':
    print(f"Модуль mymodule (версия {VERSION}) загружен как главная программа.")
    hello()
    x = float(input('Введите x: '))
    y1, y2 = calc_expression(x)
    print(f'y1 = {y1:.4f}, y2 = {y2:.4f}')
    mas, mult, s = process_array(10)
    print('Массив:', ['{:.2f}'.format(v) for v in mas])
    print(f'mult = {mult:.2f}, sum = {s:.2f}')
    A, zero_cols, row_series = process_matrix(4)
    print('Матрица:')
    for row in A:
        print(' '.join(f'{x:2d}' for x in row))
    print('Столбцов с нулём:', zero_cols)
    print('Строка с длиннейшей серией:', row_series)