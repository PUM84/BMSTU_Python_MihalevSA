from ast import Number, BinOp, Print


class CodeGenerator:
    """Генератор Python-кода из AST"""

    def generate(self, ast_nodes):
        """Генерирует Python код из списка AST узлов"""
        python_lines = []

        for node in ast_nodes:
            if isinstance(node, Print):
                # Генерируем код для print
                expr_code = self._generate_expr(node.expr)
                python_lines.append(f"print({expr_code})")

        return '\n'.join(python_lines)

    def _generate_expr(self, node):
        """Генерирует код для выражения"""
        if isinstance(node, Number):
            return str(node.value)

        elif isinstance(node, BinOp):
            left = self._generate_expr(node.left)
            right = self._generate_expr(node.right)

            op_map = {
                '+': '+',
                '-': '-',
                '*': '*',
                '/': '/',
                '^': '**'
            }
            op = op_map.get(node.op, node.op)

            return f"({left} {op} {right})"

        else:
            raise ValueError(f"Неизвестный тип узла: {type(node)}")