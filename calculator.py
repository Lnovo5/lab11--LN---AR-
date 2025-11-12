import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        math.div(b, a)
    except ValueError:
        print("Dividing by zero is illegal!")
    
def log(a, b):
    try:
        math.log(b, a)
    except ValueError:
        print("Don't use a logarithm on a number that is 0 or less!")
    
def exp(a, b):
    return math.pow(a, b)



