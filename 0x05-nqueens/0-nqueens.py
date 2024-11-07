#!/usr/bin/python3
"""
N-Queens Using Backtracking & Bit Manipulation
"""
import sys
from typing import List

input = sys.argv[1:]
if len(input) != 1:
    print("Usage: nqueens N")
    exit(1)
num = input[0]
try:
    num = int(num)
except ValueError:
    print("N must be a number")
    exit(1)
if num < 4:
    print("N must be at least 4")
    exit(1)


def solveNQueens(n: int) -> List[List[int]]:
    solutions = []
    backtrack(n, 0, 0, 0, 0, [], solutions)
    return solutions


def backtrack(n, r, c, d1, d2, board, solutions):
    if r == n:
        solutions.append([row for row in board])
        return

    for col in range(n):
        col_bit = 1 << col
        diag1_bit = 1 << (r - col + n - 1)
        diag2_bit = 1 << (r + col)

        if (c & col_bit) or (d1 & diag1_bit) or (d2 & diag2_bit):
            continue

        board.append([r, col])

        backtrack(
            n,
            r + 1,
            c | col_bit,
            d1 | diag1_bit,
            d2 | diag2_bit,
            board,
            solutions
        )
        board.pop()


for res in solveNQueens(num):
    print(res)
