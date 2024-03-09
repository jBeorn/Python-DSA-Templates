import math


def gcd(x: int, y: int):
    """
    greatest common divisor of x and y
    math.gcd(x, y)
    """
    while y:
        x, y = y, x % y
    return x