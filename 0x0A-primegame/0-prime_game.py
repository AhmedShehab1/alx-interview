#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x: int, nums: list) -> str:
    """
    Returns the winner of the Prime Game
    Args:
        x (int): Number of rounds
        nums (list): Array of n

    Returns:
        str: Winner
    """
    winners_freq = {
        "Ben": 0,
        "Maria": 0,
    }

    def sieve_of_eratosthenes(n: int) -> list:
        is_prime = [True] * (n + 1)
        primes = []

        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

        return primes

    for round in range(x):
        # generate primes for this round
        primes_round = sieve_of_eratosthenes(nums[round])
        if primes_round and len(primes_round) % 2 == 0:
            winners_freq['Maria'] += 1
        else:
            winners_freq['Ben'] += 1

    if winners_freq['Ben'] == winners_freq['Maria']:
        return None

    return 'Ben' if winners_freq['Ben'] > winners_freq['Maria'] else 'Maria'
