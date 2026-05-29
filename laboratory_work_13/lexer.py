from rply import LexerGenerator

class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('PRINT', r'print')
        self.lexer.add('GEN', r'gen')

        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')

        self.lexer.add('LPAREN', r'\(')
        self.lexer.add('RPAREN', r'\)')
        self.lexer.add('SEMICOLON', r';')

        self.lexer.add('NUMBER', r'\d+')

        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'#[^\n]*')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()