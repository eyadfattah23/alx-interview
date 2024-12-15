#!/usr/bin/python3
"""solve the prime game problem in readme"""


def isprime(x):
    """checks if x is prime
    """

    if x == 1 or x == 0 or x == -1:
        return False

        # Iterate from 2 to n // 2
    for i in range(2, (x//2)+1):
        # If x is divisible by any number between
        # 2 and n / 2, it is not prime
        if (x % i) == 0:
            return False

    return True


def get_next_prime_in_list(prev_prime_idx, list):
    """retrieves the next prime index in list
        starting iteration from the previous prime number
            in list
    """
    if prev_prime_idx >= len(list) - 1:
        return None

    for num in (list):
        if isprime(num):
            return num

    return None


def get_all_divisables(num, max):
    """get a list all numbers that are divisible by num
        and less than or equal max
    """

    return [i for i in range(num, max) if i % num == 0]


def create_dict_of_status(list):
    """create a dict to know if a number
        is removed for the round list or not
    """
    result = {}
    for i in list:
        result[i] = 0
    return result


def isWinner(x, nums):
    """#+
    Determines the winner of a game between Maria and Ben
        based on the given list of numbers.#+
#+
    Parameters:#+
    x (int): An unused parameter.#+
    nums (list of +ve ints): the number of elements in each round.#+
#+
    Returns:#+
    str: The name of the winner ("Ben" or "Maria").#+
    """  # +
    Maria_Total = 0
    Ben_Total = 0
    game_results = {}

    for round in range(x):
        if round in game_results:
            winner = game_results[round]
            if winner == 'B':
                Ben_Total += 1
            else:
                Maria_Total += 1
                continue
        round_list = list(range(1, nums[round] + 1))
        turn = 1
        ben = 0
        maria = 0

        while True:
            next_prime_idx = get_next_prime_in_list(0, round_list)
            if next_prime_idx:
                round_list = list(
                    set(round_list) -
                    set(get_all_divisables(next_prime_idx,
                                           round_list[-1] + 1)))
            else:
                if turn % 2 == 1:
                    ben += 1
                else:
                    maria += 1
                break

            turn += 1
        if ben > maria:
            game_results[round] = 'B'
            Ben_Total += 1
        else:
            game_results[round] = 'M'
            Maria_Total += 1

    if Ben_Total > Maria_Total:
        return "Ben"
    elif Maria_Total > Ben_Total:
        return "Maria"
    return None


""" print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

print(get_next_prime_in_list(4, [1, 2, 3, 4, 5, 6, 7]))
print(get_all_divisables(2, 8)) """

# print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
# print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
