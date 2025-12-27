class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f"Token({self.type}, {repr(self.value)})"
        return f"Token({self.type})"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char and self.current_char != '\n':
            self.advance()
        if self.current_char == '\n':
            self.advance()

    def number(self):
        result = ''
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return float(result) if '.' in result else int(result)

    def identifier(self):
        result = ''
        while self.current_char and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '#':
                self.skip_comment()
                continue

            if self.current_char.isdigit():
                return Token('NUMBER', self.number())

            if self.current_char.isalpha():
                ident = self.identifier()
                if ident == 'print':
                    return Token('PRINT', 'print')
                elif ident == 'gen':
                    return Token('GEN', 'gen')
                else:
                    raise ValueError(f'Неизвестная команда: {ident}')

            # Операторы и скобки
            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')

            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')

            if self.current_char == '*':
                self.advance()
                return Token('MULTIPLY', '*')

            if self.current_char == '/':
                self.advance()
                return Token('DIVIDE', '/')

            if self.current_char == '^':
                self.advance()
                return Token('POWER', '^')

            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')

            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')

            if self.current_char == ';':
                self.advance()
                return Token('SEMICOLON', ';')

            raise ValueError(f'Неизвестный символ: {repr(self.current_char)}')

        return Token('EOF')