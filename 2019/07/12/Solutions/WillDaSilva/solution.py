import ast
import operator as op

def arith_eval(expression):
    ops = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv}
    bop = lambda node: ops[type(node.op)](_arith_eval(node.left), _arith_eval(node.right))
    def _arith_eval(node):
        if isinstance(node, ast.Num):       return node.n
        elif isinstance(node, ast.BinOp):   return bop(node)
        else:                               raise TypeError(node)
    return _arith_eval(ast.parse(expression, mode='eval').body)

