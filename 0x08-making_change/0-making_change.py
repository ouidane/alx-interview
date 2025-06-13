#!/usr/bin/python3
"""Module that contains makeChange function"""


def makeChange(coins, total):
    """Determines the fewest number of coins to meet total"""
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total >= coin:
            num = total // coin
            count += num
            total -= coin * num

    return count if total == 0 else -1
