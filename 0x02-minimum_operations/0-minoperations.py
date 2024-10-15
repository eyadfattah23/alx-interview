#!/usr/bin/python3
'''
Define a method that calculates the fewest number of operations needed
to result in exactly n H characters in a file.

executing only two operations in this file: Copy All and Paste.

* Prototype: def minOperations(n)
* Returns an integer
* If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All
=> Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
'''
from math import sqrt


def minOperations(n):
    """calculates the fewest number of operations needed
            to result in exactly n H characters.

    Args:
        n (int): number of 'H' characters.
    """

    if n == 0:
        return 0
    n_prime_factors = []

    while n % 2 == 0:
        n /= 2
        n_prime_factors.append(2)

    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            n /= i
            n_prime_factors.append(i)

    if n > 2:
        n_prime_factors.append(n)

    return int(sum(n_prime_factors))


"""
print(minOperations(9))
print(minOperations(12))
print(minOperations(18))
print(minOperations(4))
print(minOperations(5))
print(minOperations(100))
print(minOperations(137))
 """
