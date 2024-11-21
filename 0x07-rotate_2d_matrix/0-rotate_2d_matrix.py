#!/usr/bin/python3
"""
scrip to rotate a Given n x n 2D matrix,
        by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """rotate matrix by 90 degrees clockwise

    Args:
        matrix (list[list[int]]): 2d matrix to rotate
    """
    n = len(matrix)

    """ for i in range(0, n // 2):
        for j in range(i, n-i-1):
            print(f"temp = ({j}, {i})", matrix[j][i])  # done
            print()  # done
            print(f"put({n-1-i},{j}) in ({j}, {i})")  # done
            print(f"put({n-1-j},{n-1-i}) in ({n-1-i}, {j})")  # done
            print(f"put({i},{n-1-j}) in ({n-1-j}, {n-1-i})")
            print(f"put temp in ({i}, {n-1-j})")
            print() """
    for i in range(0, n//2):
        for j in range(i, n-i-1):

            temp = matrix[j][i]
            matrix[j][i] = matrix[n-1-i][j]
            matrix[n-1-i][j] = matrix[n-1-j][n-1-i]
            matrix[n-1-j][n-1-i] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
