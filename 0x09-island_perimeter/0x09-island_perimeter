#!/usr/bin/python3
"""
    Module that calculates the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """Function that calculates the perimeter of an island in a grid"""
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                result += 4
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    result -= 2
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    result -= 2

    return result
