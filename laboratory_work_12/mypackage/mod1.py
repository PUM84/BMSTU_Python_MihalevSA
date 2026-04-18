"""Модуль с утилитами для списков."""

def unique_elements(lst):
    """Возвращает список уникальных элементов."""
    return list(set(lst))

def flatten(nested_list):
    """Преобразует вложенный список в плоский."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result