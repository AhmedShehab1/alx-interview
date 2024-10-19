#!/usr/bin/python3
"""
0-minoperations.py
"""
import math


def getPrimeFactorization(number: int) -> list:
    """
    returns a list containing prime factorization of number
    Args:
        number (int): number to get factorization of

    Returns:
        list: A list containing the prime factorization
              of the input if possible
    """
    res = []

    if number <= 3:
        res.append(number)
        return res

    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            number = number // i
            res.append(i)
    return res


def minOperations(n: int) -> int:
    """
    function to compute the minimum
    operations required using only
    Copy All and Paste Commands
    starting from a single char 'H'
    to reach to n H's
    Args:
        n (int): desired number to reach

    Returns:
        int: minimum number of operations required
    """
    fac = getPrimeFactorization(n)
    if fac[0] != 2 and fac[0] != 3:
        return 0
    return sum(fac)
