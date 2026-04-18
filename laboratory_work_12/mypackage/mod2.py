"""Модуль с математическими функциями."""

def is_prime(n):
    """Проверка числа на простоту."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Возвращает n-е число Фибоначчи."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a