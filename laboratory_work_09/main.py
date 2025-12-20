print("=" * 50)
print("КАЛЬКУЛЯТОР С ПРИОРИТЕТАМИ")
print("=" * 50)
print("\nКак использовать:")
print("  print(2 + 3 * 4);")
print("  print((2 + 3) * 4);")
print("  print(2 ^ 3);   # возведение в степень")
print("  print(10 / 2);  # деление")
print("  # комментарий")
print("  exit - выход")
print("\nПриоритет операций:")
print("  1. Скобки ()")
print("  2. Возведение в степень ^")
print("  3. Умножение * и деление /")
print("  4. Сложение + и вычитание -")
print("-" * 50)

import sys

sys.path.append('.')
from lexer import Lexer
from parser import Parser

while True:
    try:
        user_input = input("\n> ").strip()

        if user_input.lower() in ('exit', 'quit'):
            print("До свидания!")
            break

        if not user_input or user_input.startswith('#'):
            continue

        # Запускаем интерпретатор
        lexer = Lexer(user_input)
        parser = Parser(lexer)
        statements = parser.parse()

        for statement in statements:
            statement.eval()

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")