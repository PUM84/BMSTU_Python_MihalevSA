from rply import ParserGenerator
from ast import Number, BinaryOp, Print, Gen

class Parser:
    def __init__(self, codegen):
        self.codegen = codegen
        self.pg = ParserGenerator(
            tokens=['NUMBER', 'PRINT', 'GEN', 'PLUS', 'MINUS', 'MUL', 'DIV',
                    'LPAREN', 'RPAREN', 'SEMICOLON'],
            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV']),
            ]
        )

    def parse(self):
        @self.pg.production('program : statements')
        def program(p):
            class Program:
                def __init__(self, stmts):
                    self.statements = stmts
                def eval(self):
                    for stmt in self.statements:
                        stmt.eval()
                def interpret(self):
                    for stmt in self.statements:
                        stmt.interpret()
            return Program(p[0])

        @self.pg.production('statements : statement')
        @self.pg.production('statements : statement statements')
        def statements(p):
            if len(p) == 1:
                return [p[0]]
            return [p[0]] + p[1]

        @self.pg.production('statement : PRINT LPAREN expression RPAREN SEMICOLON')
        def statement_print(p):
            return Print(self.codegen, p[2])

        @self.pg.production('statement : GEN LPAREN expression RPAREN SEMICOLON')
        def statement_gen(p):
            return Gen(self.codegen, p[2])

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_binop(p):
            return BinaryOp(self.codegen, p[0], p[1].gettokentype(), p[2])

        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return Number(self.codegen, p[0].value)

        @self.pg.production('expression : LPAREN expression RPAREN')
        def expression_paren(p):
            return p[1]

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Синтаксическая ошибка: {token.gettokentype()} '{token.getstr()}'")

    def get_parser(self):
        return self.pg.build()