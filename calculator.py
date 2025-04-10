#https://github.com/elizabethjang/lab10-EJ-DR.git
#Partner 1: Elizabeth Jang
#Partner 2: Derek Rosales
# First example
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError
def logarithm(a, b):
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
def hypotenuse(a, b):
    return (a**2 + b**2)**0.5
def square_root(a):
    return a ** 0.5