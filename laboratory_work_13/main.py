import sys
from lexer import Lexer
from parser import Parser
from codegen import CodeGen

def run_program(source_code, mode='jit'):
    """
    mode: 'jit' – компиляция и выполнение через LLVM
          'interp' – интерпретация без LLVM (для отладки)
    """
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(source_code)

    cg = CodeGen()
    parser = Parser(cg)
    parser.parse()
    pg = parser.get_parser()

    ast = pg.parse(tokens)

    if mode == 'jit':
        ast.eval()
        cg.finalize()
        cg.run()
    else:
        ast.interpret()

def main():
    print("Лабораторная работа №13 – Компилятор на LLVM")
    print("Команды: print(выражение);  gen(выражение);")
    print("Для выхода введите 'exit' или 'quit'")

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            run_program(code, mode='jit')
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
        return

    while True:
        try:
            line = input(">> ").strip()
            if line.lower() in ('exit', 'quit'):
                break
            if not line or line.startswith('#'):
                continue
            run_program(line, mode='jit')
        except EOFError:
            break
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()