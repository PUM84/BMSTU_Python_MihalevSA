import ctypes
import sys

class MyList:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.array = (self.capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        new_array = (new_capacity * ctypes.py_object)()
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.length] = item
        self.length += 1

    def insert(self, index, item):
        if index < 0:
            index = self.length + index + 1
        if index < 0:
            index = 0
        if index > self.length:
            index = self.length
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.length += 1

    def delete(self, index):
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            raise IndexError("Индекс вне диапазона")
        deleted = self.array[index]
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1
        if self.length <= self.capacity // 2 and self.capacity > 8:
            self._resize(max(self.capacity // 2, 8))
        return deleted

    def pop(self, index=None):
        if index is None:
            if self.length == 0:
                raise IndexError("Удаление из пустого списка")
            self.length -= 1
            deleted = self.array[self.length]
            if self.length <= self.capacity // 2 and self.capacity > 8:
                self._resize(max(self.capacity // 2, 8))
            return deleted
        else:
            return self.delete(index)

    def remove(self, value):
        for i in range(self.length):
            if self.array[i] == value:
                self.delete(i)
                return
        raise ValueError(f"Значение {value} не найдено в списке")

    def clear(self):
        self.length = 0
        self.capacity = 8
        self.array = (self.capacity * ctypes.py_object)()

    def index(self, value):
        for i in range(self.length):
            if self.array[i] == value:
                return i
        raise ValueError(f"Значение {value} не найдено в списке")

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            raise IndexError("Индекс вне диапазона")
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            raise IndexError("Индекс вне диапазона")
        self.array[index] = value

    def __contains__(self, item):
        for i in range(self.length):
            if self.array[i] == item:
                return True
        return False

    def __str__(self):
        if self.length == 0:
            return "[]"
        parts = [str(self.array[i]) for i in range(self.length)]
        return "[" + ", ".join(parts) + "]"


if __name__ == "__main__":
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА MyList")
    print("=" * 60)

    my_list = MyList()
    print(f"Создан пустой список: {my_list}")
    print(f"Длина: {len(my_list)}, Capacity: {my_list.capacity}")

    print("\n--- 1. Добавление элементов (append) ---")
    for i in range(5):
        my_list.append(f"элемент_{i}")
        print(f"  Добавлен: элемент_{i} -> {my_list}")

    print("\n--- 2. Вставка в начало (insert(0, 'НОВЫЙ_В_НАЧАЛО')) ---")
    my_list.insert(0, "НОВЫЙ_В_НАЧАЛО")
    print(f"  Результат: {my_list}")

    print("\n--- 3. Вставка в середину (insert(3, 'В_СЕРЕДИНУ')) ---")
    my_list.insert(3, "В_СЕРЕДИНУ")
    print(f"  Результат: {my_list}")

    print("\n--- 4. Вставка в конец (insert(100, 'В_КОНЕЦ')) ---")
    my_list.insert(100, "В_КОНЕЦ")
    print(f"  Результат: {my_list}")

    print("\n--- 5. Вставка с отрицательным индексом (insert(-2, 'ПРЕДПОСЛЕДНИЙ')) ---")
    my_list.insert(-2, "ПРЕДПОСЛЕДНИЙ")
    print(f"  Результат: {my_list}")

    print("\n--- 6. Удаление по индексу (delete(2)) ---")
    deleted = my_list.delete(2)
    print(f"  Удалён элемент: '{deleted}'")
    print(f"  Результат: {my_list}")

    print("\n--- 7. Удаление последнего элемента (pop()) ---")
    deleted = my_list.pop()
    print(f"  Удалён элемент: '{deleted}'")
    print(f"  Результат: {my_list}")

    print("\n--- 8. Удаление с отрицательным индексом (pop(-3)) ---")
    deleted = my_list.pop(-3)
    print(f"  Удалён элемент: '{deleted}'")
    print(f"  Результат: {my_list}")

    print("\n--- 9. Удаление по значению (remove('элемент_2')) ---")
    my_list.remove("элемент_2")
    print(f"  Результат: {my_list}")

    print("\n--- 10. Попытка удалить несуществующее значение ---")
    try:
        my_list.remove("НЕСУЩЕСТВУЕТ")
    except ValueError as e:
        print(f"  Ошибка: {e}")

    print("\n--- 11. Проверка наличия элемента (__contains__) ---")
    print(f"  'элемент_1' в списке: {'элемент_1' in my_list}")
    print(f"  'элемент_999' в списке: {'элемент_999' in my_list}")

    print("\n--- 12. Получение индекса элемента (index) ---")
    if "элемент_3" in my_list:
        idx = my_list.index("элемент_3")
        print(f"  Индекс 'элемент_3': {idx}")

    print("\n--- 13. Изменение элемента по индексу (__setitem__) ---")
    my_list[1] = "ИЗМЕНЁННЫЙ"
    print(f"  Результат: {my_list}")

    print("\n--- 14. Получение элемента по индексу (__getitem__) ---")
    print(f"  my_list[0] = '{my_list[0]}'")
    print(f"  my_list[-1] = '{my_list[-1]}'")

    print("\n--- 15. Очистка списка (clear) ---")
    my_list.clear()
    print(f"  Результат: {my_list}")
    print(f"  Длина: {len(my_list)}")

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ АВТОМАТИЧЕСКОГО ИЗМЕНЕНИЯ CAPACITY")
    print("=" * 60)

    demo = MyList()
    print(f"Начальная capacity: {demo.capacity}")

    print("\nДобавление элементов (append):")
    for i in range(20):
        demo.append(i)
        print(f"  len={len(demo):2}, capacity={demo.capacity}")

    print("\nУдаление элементов (pop):")
    for i in range(20):
        demo.pop()
        print(f"  len={len(demo):2}, capacity={demo.capacity}")

    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ С ВСТРОЕННЫМ СПИСКОМ PYTHON")
    print("=" * 60)

    custom = MyList()
    native = []

    print("\nДобавление 10 элементов:")
    for i in range(10):
        custom.append(i)
        native.append(i)
        print(f"  MyList: {custom}")
        print(f"  list: {native}")

    print("\nВставка 'ВСТАВКА' на позицию 3:")
    custom.insert(3, "ВСТАВКА")
    native.insert(3, "ВСТАВКА")
    print(f"  MyList: {custom}")
    print(f"  list: {native}")

    print("\nУдаление элемента с позиции 5:")
    del_custom = custom.pop(5)
    del_native = native.pop(5)
    print(f"  Удалено из MyList: '{del_custom}'")
    print(f"  Удалено из list: '{del_native}'")
    print(f"  MyList: {custom}")
    print(f"  list: {native}")