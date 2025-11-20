import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
# https://github.com/Lnovo5/lab11--LN---AR-/tree/main
# Partner 1: Lucia Novo
# Partner 2: Afnan Rehan



def square_root(a):
    if a < 0:
        raise ValueError("You cannot find the square root of a negative!")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)


def exp(a, b):
    return a ** b


