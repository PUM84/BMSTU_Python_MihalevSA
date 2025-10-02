from random import randint

n = int(input("Введите размер квадратной матрицы (N): "))

A = [[randint(0, 9) for _ in range(n)] for _ in range(n)]

print("\nМатрица A:")
for row in A:
    print(' '.join(f"{x:2d}" for x in row))


count_cols_with_zero = sum(any(A[row][col] == 0 for row in range(n)) for col in range(n))
print("\nКоличество столбцов с хотя бы одним нулём:", count_cols_with_zero)

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

print("Номер строки с самой длинной серией одинаковых элементов:", row_with_max_series + 1)
