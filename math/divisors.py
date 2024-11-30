

def getDivs(num):
    """
    returns all divisors of num
    """
    divisors = []
    for d in range(1, int(num**0.5) + 1):
        if num % d == 0:
            divisors.append(d)
            # Avoid adding the square root twice if it's a perfect square
            if d != num//d:
                divisors.append(num//d)
    return sorted(divisors)