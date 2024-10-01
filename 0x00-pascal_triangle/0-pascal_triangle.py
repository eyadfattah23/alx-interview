#!/usr/bin/python3
"""
a function def pascal_triangle(n):
    return list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing Pascal triangle of n

    Returns an empty list if n <= 0
    You can assume n will be always an integer

    Args:
        n (int): number of lists in th the triangle
    """

    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    result = [[1], [1, 1]]

    if n == 2:
        return result

    def pascal_triangle_helper(result, n):
        """recursive function for pascal triangulation"""
        if len(result) == n:
            return result

        prev = result[-1]
        new = [1]
        new_result = result
        for i in range(0, len(prev)):
            try:
                new.append(prev[i] + prev[i + 1])
            except IndexError:
                new.append(1)
                new_result.append(new)
                break
        return pascal_triangle_helper(result, n)

    return pascal_triangle_helper(result, n)
