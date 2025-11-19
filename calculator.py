import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    try:
        return math.sqrt(a)
    except:
        print("You cannot find the square root of a negative!")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return math.div(b, a)
    except ValueError:
        print("Dividing by zero is illegal!")
    
def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        print("Don't use a logarithm on a number that is 0 or less!")
    
def exp(a, b):
    return math.pow(a, b)



