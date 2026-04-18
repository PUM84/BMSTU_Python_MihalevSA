import sys

sys.path.append('.')

from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator

while True:
    try:
        user_input = input("> ").strip()

        if user_input.lower() in ('exit', 'quit'):
            break

        if not user_input or user_input.startswith('#'):
            continue

        lexer = Lexer(user_input)
        parser = Parser(lexer)

        try:
            statements = parser.parse()
        except Exception as e:
            print(f"Ошибка парсинга: {e}")
            continue

        if user_input.startswith('gen('):
            generator = CodeGenerator()
            python_code = generator.generate(statements)
            print(python_code)
        else:
            for statement in statements:
                statement.eval()

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")