from django.shortcuts import render
from django.http import HttpResponse
import ast
import operator as op

# Supported operators
SAFE_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}


def safe_eval(expr):
    """
    Evaluate a math expression safely using AST.
    Allowed: +, -, *, /, %, ** and parentheses.
    """

    def _eval(node):
        if isinstance(node, ast.BinOp):
            return SAFE_OPERATORS[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return SAFE_OPERATORS[type(node.op)](_eval(node.operand))
        elif isinstance(node, ast.Num):  # For Python < 3.8
            return node.n
        elif isinstance(node, ast.Constant):  # For Python >= 3.8
            return node.value
        else:
            raise ValueError("Unsupported operation")

    try:
        parsed_expr = ast.parse(expr, mode='eval').body
        return _eval(parsed_expr)
    except Exception:
        raise ValueError("Invalid Expression")


def home(request):
    return HttpResponse("Welcome to the Calculator App!")


def index(request):
    return render(request, 'index.html')


def submit_query(request):
    q = request.GET.get('query')
    try:
        answer = safe_eval(q)
        return render(request, 'index.html', {
            'q': q,
            'answer': answer,
            'error': False
        })
    except:
        return render(request, 'index.html', {
            'q': q,
            'answer': None,
            'error': True
        })
