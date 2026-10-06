import ast
import operator as op

_ALLOWED = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}

def calculate(expression: str) -> float | int:
    """Safely evaluate basic arithmetic only."""
    tree = ast.parse(expression, mode="eval")

    def visit(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
            return _ALLOWED[type(node.op)](visit(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
            return _ALLOWED[type(node.op)](visit(node.left), visit(node.right))
        raise ValueError("Only basic arithmetic is allowed.")

    return visit(tree.body)
