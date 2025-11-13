import math

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def add(a, b): a + b

def subtract(a, b): a - b

def multiply(a, b): a * b

def divide(a, b): b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b): loga(b)# use math library/raise ValueError

def exponent(a, b): ab

