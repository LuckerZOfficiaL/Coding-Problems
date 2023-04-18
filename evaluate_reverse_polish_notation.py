# -*- coding: utf-8 -*-
"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.


Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    
    
Idea: use a Stack
"""

def eval_polish(expr):
    stack = []
    for i in range(0, len(expr)):
        if expr[i] == "+":
            Sum = stack[-2] + stack[-1]
            stack.pop()
            stack[-1] = Sum
        elif expr[i] == "-":
            Dif = stack[-2] - stack[-1]
            stack.pop()
            stack[-1] = Dif
        elif expr[i] == "*":
            Prod = stack[-2] * stack[-1]
            stack.pop()
            stack[-1] = Prod
        elif expr[i] == "/":
            Quot = stack[-2] / stack[-1]
            stack.pop()
            stack[-1] = Quot
        else:
            stack.append(int(expr[i]))
        i += 1
    return stack[0]


print(eval_polish(["2","1","+","3","*"]))
print(eval_polish(["4","13","5","/","+"]))
print(eval_polish(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
        
    
