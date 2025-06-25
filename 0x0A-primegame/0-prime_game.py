#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game."""


def isWinner(x, nums):
    """
    Determines the winner of each round of the game.
    Arguments:
        x: number of rounds
        nums: list of integers, each representing the set size for a round
    Returns:
        "Maria" if Maria wins more rounds,
        "Ben" if Ben wins more rounds,
        None if the number of wins is equal
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes to identify primes up to max_n
    is_prime = [False, False] + [True] * (max_n - 1)
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Compute prefix sum of prime counts
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
