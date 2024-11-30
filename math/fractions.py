import math
# import fractions

def addFractions(num1: int, den1: int, num2: int, den2: int, op: str):
    commonDen = math.lcm(den1, den2)
    nnum1 = num1 * (commonDen // den1)
    nnum2 = num2 * (commonDen // den2)
    if op == "+":
        nnum = nnum1 + nnum2
    elif op == "-":
        nnum = nnum1 - nnum2
    commonDiv = math.gcd(nnum, commonDen)
    return f"{nnum // commonDiv}/{commonDen // commonDiv}"