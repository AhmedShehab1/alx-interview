#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid) -> int:
    """
    returns perimeter of the island described in grid
    Args:
        grid (List[List]): list of list of integers

    Returns:
        int: perimeter of the island described in grid
    """
    m, n = len(grid), len(grid[0])
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1
    return perimeter
