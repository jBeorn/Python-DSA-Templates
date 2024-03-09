import math


def gcd(x: int, y: int):
    """
    greatest common divisor of x and y
    math.gcd(x, y)
    """
    while y:
        x, y = y, x % y
    return x

def lcm(x: int, y: int):
    """
    Least Common Multiple of x and y
    """
    return (x * y) // gcd(x, y)

def lcm_of_multiple(numbers: list):
    """
    Least Common Multiple of a list
    math.lcm([n1, n2, n3...])
    """
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        lcm_result = numbers[0]
        for i in range(1, len(numbers)):
            lcm_result = lcm(lcm_result, numbers[i])
        return lcm_result