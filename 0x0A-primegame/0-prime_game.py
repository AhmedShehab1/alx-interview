#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x: int, nums: list) -> str:
    """
    Determines the winner of the Prime Game
    Args:
        x (int): Number of rounds
        nums (list): Array of integers representing each round's max number.

    Returns:
        str: The winner ( "Maria" or "Ben" ) or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    winners_freq = {
        "Ben": 0,
        "Maria": 0,
    }

    for n in nums:
        if prime_count[n] % 2 == 0:
            winners_freq["Ben"] += 1
        else:
            winners_freq["Maria"] += 1

    if winners_freq["Ben"] == winners_freq["Maria"]:
        return None

    return "Ben" if winners_freq["Ben"] > winners_freq["Maria"] else "Maria"
