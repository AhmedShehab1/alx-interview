#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns list of lists of integers representing pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(2, n + 1):
        arr = [1]
        if (len(triangle[-1])) >= 2:
            arr.extend([triangle[-1][k] + triangle[-1][k + 1]
                       for k in range(len(triangle[-1]) - 1)])
        arr.append(1)
        triangle.append(arr)
    return triangle
