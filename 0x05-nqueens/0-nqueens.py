#!/usr/bin/python3
"""
Task 0: N queens
"""

import sys


def canMove(final, row, column):
    """
    Checks if the queen would be able to move
    """
    rows = []
    columns = []
    top_left = []
    top_right = []

    for nums in final:
        rows.append(nums[0])
        columns.append(nums[1])
        top_left.append(nums[1] - nums[0])
        top_right.append(nums[0] + nums[1])

    if row in rows or column in columns:
        return False
    if column - row in top_left or row + column in top_right:
        return False

    return True


def nqueens(final, column, checked_queens=[]):
    """
    The main recursive program
    """
    for item in range(n):
        if canMove(final, item, column):
            final.append([item, column])
            if column == n - 1:
                checked_queens.append(final.copy())
                del final[-1]
            else:
                nqueens(final, column + 1)

    if len(final) > 0:
        del final[-1]
    return checked_queens

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    final = []
    final = nqueens(final, 0)

    for nums in final:
        print(nums)
