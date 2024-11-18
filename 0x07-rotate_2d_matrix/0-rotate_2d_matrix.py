#!/usr/bin/python3
"""
Rotate 2D Matrix by 90 degree
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotates 2D Matrix by 90 degree
    Args:
        matrix (List[List]): 2D int Matrix
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
