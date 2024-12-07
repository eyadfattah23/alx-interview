#!/usr/bin/python3
"""Script to find the minimum number of coins to makes a given total amount"""


def coin_dp(coins, total, memo=None):
    """Finds minimum number of coins required to make a given total using DP

    Args:
        coins: list of integers representing the available coin denominations
        total: The target total amount to be reached using the given coins.
        memo: A memoization dictionary to store previously computed results.

    Returns:
        list of coins used to make up the total if a solution exists,
        or None if it's impossible to reach the total with the given coins.
    """
    if memo is None:
        memo = {}
    if total in memo:
        return memo[total]
    if total == 0:
        return []
    if total < 0:
        return None

    shortest_way = None
    for coin in coins:
        subtraction = coin_dp(coins, total - coin, memo)
        if subtraction is not None:
            current_edges = subtraction + [coin]
            if shortest_way is None or len(current_edges) < len(shortest_way):
                shortest_way = current_edges

    memo[total] = shortest_way
    return memo[total]


def make_change2(coins, total, coin_idx=0, memo=None):
    """Calculates the minimum number of coins needed to make a given total.

    Args:
        coins: Integer values representing coins available.
        total: Target total amount to be reached using the given coins.
        coin_idx: The current index in the coins list being considered.
        memo: A memoization dictionary to store previously computed results.

    Returns:
        The minimum number of coins needed to reach the total.
        Returns float('inf')
            if it's impossible to reach the total with given coins
    """
    if memo is None:
        memo = {}

    if (total, coin_idx) in memo:
        return memo[(total, coin_idx)]

    if total in coins:
        memo[(total, coin_idx)] = 1
        return 1

    if total == 0:
        return 0

    if total < 0 or coin_idx >= len(coins):
        return float('inf')

    res = -1

    if coins[coin_idx] > total:
        remainder2 = make_change2(coins, total, coin_idx + 1, memo)
        res = remainder2
    else:
        remainder1 = 1 + \
            make_change2(coins, total - coins[coin_idx], coin_idx, memo)
        remainder2 = make_change2(coins, total, coin_idx + 1, memo)
        res = min(remainder1, remainder2)

    memo[(total, coin_idx)] = res
    return res


def makeChange(coins, total):
    """Calculates the minimum number of coins needed to make a given total.

    Args:
        coins: A list of coin denominations.
        total: The target total amount.

    Returns:
        The minimum number of coins needed to reach the total,
            or -1 if it's impossible.
    """
    if len(coins) == 1 and total not in coins:
        return -1

    coins.sort(reverse=True)
    result = make_change2(coins, total, 0)
    return result if result != float('inf') else -1


# Example usage:
# print(make_change2([5, 2, 1], 11))
# print(coin_dp([5, 4, 3, 7], 7))
# print(make_change([7, 4, 3, 5], 7))
# print(coin_dp([25, 2, 1], 37))
# print(make_change([25, 2, 1], 29))
# print(make_change2([1256, 102, 54, 48, 16], 1453))
# print(make_change2([25, 2, 1], 37))
# print(make_change2([25, 2, 1], 29))
# print(make_change2([7, 4, 3, 5], 7))
# print(make_change2([1, 4, 3, 7], 7))
# print(make_change([2], 3))
# print(make_change([1], 1))
# print(makeChange([3, 7, 405, 436], 8839))
