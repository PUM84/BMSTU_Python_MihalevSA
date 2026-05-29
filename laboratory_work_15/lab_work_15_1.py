# laboratory_work_15.py

import ctypes
import sys

my_variable = 42
print(f"Значение переменной: {my_variable}")
adress_my_variable = id(my_variable)
print(f"Адрес объекта переменной: {hex(adress_my_variable)}")
object_by_adress = ctypes.cast(adress_my_variable, ctypes.py_object)
print(f"Объект по адресу: {object_by_adress}")
print(f"Значение переменной: {object_by_adress.value}")
print()

my_list = []
print("Добавляем элементы в массив:")
print(f"Размер списка из {len(my_list)} элементов: {sys.getsizeof(my_list)} байт.")
for i in range(20):
    my_list.append(i)
    print(f"Размер списка из {len(my_list)} элементов: {sys.getsizeof(my_list)} байт.")

print("\nУдаляем элементы из массива:")
for i in range(20):
    my_list.pop()
    print(f"Размер списка из {len(my_list)} элементов: {sys.getsizeof(my_list)} байт.")