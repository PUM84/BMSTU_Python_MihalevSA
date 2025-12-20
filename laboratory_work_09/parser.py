from ast import Number, BinOp, Print


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError(f'Ожидался {token_type}, получен {self.current_token.type}')

    def parse(self):
        statements = []
        while self.current_token.type != 'EOF':
            statements.append(self.statement())
        return statements

    def statement(self):
        if self.current_token.type == 'PRINT':
            return self.print_statement()
        else:
            raise ValueError(f'Неожиданная команда: {self.current_token.type}')

    def print_statement(self):
        self.eat('PRINT')
        self.eat('LPAREN')

        expr = self.expr()

        self.eat('RPAREN')
        self.eat('SEMICOLON')

        return Print(expr)

    def expr(self):
        """Сложение и вычитание"""
        node = self.term()

        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token.value, right=self.term())

        return node

    def term(self):
        """Умножение и деление"""
        node = self.factor()

        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token.value, right=self.factor())

        return node

    def factor(self):
        """Возведение в степень"""
        node = self.atom()

        while self.current_token.type == 'POWER':
            token = self.current_token
            self.eat('POWER')
            node = BinOp(left=node, op=token.value, right=self.atom())

        return node

    def atom(self):
        """Числа и скобки"""
        if self.current_token.type == 'NUMBER':
            value = self.current_token.value
            self.eat('NUMBER')
            return Number(value)

        elif self.current_token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node

        else:
            raise ValueError(f'Ожидалось число или скобка, получен {self.current_token.type}')