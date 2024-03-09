import math


def SieveOfEratosthenes(n: int):
    """
    returns a list of primes <= n
    """
    if n < 2:
        return [False, False]
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int((n + 1) ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def is_prime(n: int):
    """
    returns True if n is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True