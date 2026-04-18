class Number:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()

        if self.op == '+':
            return left_val + right_val
        elif self.op == '-':
            return left_val - right_val
        elif self.op == '*':
            return left_val * right_val
        elif self.op == '/':
            if right_val == 0:
                raise ValueError("Деление на ноль")
            return left_val / right_val
        elif self.op == '^':
            return left_val ** right_val


class Print:
    def __init__(self, expr):
        self.expr = expr

    def eval(self):
        result = self.expr.eval()
        print(result)


class Gen:
    """Специальный узел для генерации кода"""
    def __init__(self, expr):
        self.expr = expr