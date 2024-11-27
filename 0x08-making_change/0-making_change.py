#!/usr/bin/python3


def makeChange(coins, total):
    coins.sort(reverse=True)

    if total <= 0:
        return 0

    minimum_number_of_coins = 0

    for coin in coins:
        if coin <= total:
            count = total // coin
            total -= count * coin
            minimum_number_of_coins += count

        if total == 0:
            break

    return minimum_number_of_coins if not total else -1
