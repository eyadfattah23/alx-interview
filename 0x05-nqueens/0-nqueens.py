#!/usr/bin/python3
'''
script to solve the nqueens problem stated in the README file
'''

from sys import argv, exit


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    board_size = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if board_size < 4:
    print("N must be at least 4")
    exit(1)


boards = []


def validate_queen(board, col: int, row: int) -> bool:
    """check the new queen place in the board
        if there is a queen already in the same row, column
                or diagonals, return False

    Args:
        board (List[list[int]]):
                board to check [[row, column], [row, column], ..etc]
        row (int): row of the new queen
        col (int): column of the new queen
    """

    if len(board) == 0:
        return True

    for q_idx in range(len(board)):
        if col == board[q_idx][1] or \
                abs(row - board[q_idx][0]) == abs(col - board[q_idx][1]):
            return False

    return True


def nqueens(num, board):
    """back_tracking function to solve the nqueens problem

    Args:
        num (int): board side length
        board (List[list[int]]): board to add or remove from
    """
    if (len(board) == num):
        print(board)
        return
    row = len(board)
    for col in range(num):
        if (validate_queen(board, col, row)):
            board.append([row, col])
            nqueens(num, board)
            board.remove([row, col])
    return


nqueens(board_size, [])
