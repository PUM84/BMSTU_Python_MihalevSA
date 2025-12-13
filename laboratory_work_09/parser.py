from ast import String, Print


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

        if self.current_token.type != 'STRING':
            raise ValueError('Ожидалась строка в print()')

        string_token = self.current_token
        self.eat('STRING')
        self.eat('RPAREN')
        self.eat('SEMICOLON')

        return Print(String(string_token.value))