#!/usr/bin/python3
"""
Module to calculate the min number of operations to achieve n 'H' characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations neededto result
    in exactly n 'H' characters.

    Args:
        n (int): Target number of 'H' characters

    Returns:
        int: Minimum number of operations, or 0 if impossible
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

        if divisor * divisor > n and n > 1:
            operations += n
            break

    return operations
