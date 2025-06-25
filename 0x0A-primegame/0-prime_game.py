#!/usr/bin/python3
"""
Prime Game - isWinner function
"""

def isWinner(x, nums):
    """Determines the winner of each round and returns the overall winner"""
    if not nums or x < 1:
        return None

    max_n = max(nums)

    is_prime = [False, False] + [True] * (max_n - 1)
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n+1, i):
                is_prime[j] = False

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    for n in nums:
        if prime_count[n] % 2 != 0:
            maria_wins += 1

    if maria_wins > x // 2:
        return "Maria"
    elif maria_wins < x // 2:
        return "Ben"
    else:
        return None
