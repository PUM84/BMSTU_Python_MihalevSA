from llvmlite import ir

class Number:
    def __init__(self, codegen, value):
        self.codegen = codegen
        self.value = int(value)

    def eval(self):
        return ir.Constant(ir.IntType(32), self.value)

    def interpret(self):
        return self.value


class BinaryOp:
    def __init__(self, codegen, left, op, right):
        self.codegen = codegen
        self.left = left
        self.op = op
        self.right = right

    def eval(self):
        l = self.left.eval()
        r = self.right.eval()
        if self.op == '+':
            return self.codegen.builder.add(l, r)
        elif self.op == '-':
            return self.codegen.builder.sub(l, r)
        elif self.op == '*':
            return self.codegen.builder.mul(l, r)
        elif self.op == '/':
            return self.codegen.builder.sdiv(l, r)
        else:
            raise ValueError(f"Неподдерживаемая операция: {self.op}")

    def interpret(self):
        l = self.left.interpret()
        r = self.right.interpret()
        if self.op == '+':
            return l + r
        elif self.op == '-':
            return l - r
        elif self.op == '*':
            return l * r
        elif self.op == '/':
            return l // r if l % r == 0 else l / r
        else:
            raise ValueError(f"Неподдерживаемая операция: {self.op}")


class Print:
    def __init__(self, codegen, expr):
        self.codegen = codegen
        self.expr = expr

    def eval(self):
        value = self.expr.eval()
        self.codegen.emit_print(value)
        return value

    def interpret(self):
        res = self.expr.interpret()
        print(res)
        return res


class Gen(Print):
    """Команда gen – полный синоним print (генерирует и выполняет IR)"""
    pass