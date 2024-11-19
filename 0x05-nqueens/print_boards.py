#!/usr/bin/python3
from typing import List


class Solution:
    def __init__(self):
        self.boards = []

    def validate_queen(self, board: list, col: int, row: int) -> bool:
        if len(board) == 0:
            return True

        for q_idx in range(len(board)):
            if col == board[q_idx][1] or \
                    abs(row - board[q_idx][0]) == abs(col - board[q_idx][1]):
                return False
        return True

    def nqueens(self, num: int, board: List[List[int]]):
        if (len(board) == num):
            str_boards = []
            for i in range(len(board)):
                row, column = board[i][0], board[i][1]
                str_board = []
                for j in range(len(board)):
                    if j == column:
                        str_board.append("Q")
                    else:
                        str_board.append(".")
                str_boards.append("".join(str_board))
            self.boards.append(str_boards)
            return

        row = len(board)
        for col in range(num):
            if (self.validate_queen(board, col, row)):
                board.append([row, col])
                self.nqueens(num, board)
                board.pop()

        return

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]

        if n < 4:
            return []

        self.nqueens(n, [])
        return self.boards


sol = Solution()


sol.nqueens(5, [])


print(sol.boards)


[["Q....", "..Q..", "....Q", ".Q...", "...Q."],
 ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
 [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
 [".Q...", "....Q", "..Q..", "Q....", "...Q."],
 ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
 ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
 ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
 ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
 ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
 ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]]


[["Q....", "..Q..", "....Q", ".Q...", "...Q."],
 ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
 [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
 [".Q...", "....Q", "..Q..", "Q....", "...Q."],
 ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
 ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
 ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
 ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
 ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
 ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]]


# expected
[["Q....", "..Q..", "....Q", ".Q...", "...Q."],
 ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
 [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
 [".Q...", "....Q", "..Q..", "Q....", "...Q."],
 ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
 ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
 ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
 ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
 ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
 ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]]


# mine
[["Q....", "..Q..", "....Q", ".Q...", "...Q."],
 ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
 [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
 [".Q...", "....Q", "..Q..", "Q....", "...Q."],
 ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
 ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
 ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
 ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
 ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
 ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]]
