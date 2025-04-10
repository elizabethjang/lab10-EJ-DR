"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/elizabethjang/lab10-EJ-DR.git
#Partner 1: Elizabeth Jang
#Partner 2: Derek Rosales
# First example
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multiply(a, b):
    return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError
def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input values")
    exponent = 0
    if a < 1:
        while a < 1:
            a *= b
            exponent -= 1
    else:
        while a >= b:
            a /= b
            exponent += 1

    return exponent