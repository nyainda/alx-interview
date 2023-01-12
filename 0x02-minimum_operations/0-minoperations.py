#!/usr/bin/python3

from math import sqrt, ceil

'''This module defines a function that given a number n, minOperations(n) calculates the fewest number of operations needed to result in exactly n H characters in the file.
    Returns an integer. If n is impossible to achieve, it returns 0.
    '''
def minOperations(n):
    '''Given a number n, minOperations(n) calculates the fewest number of operations needed to result in exactly n H characters in the file.
    Returns an integer. If n is impossible to achieve, it returns 0.
    '''
    if n <= 0:
        return 0
    num = sqrt(n)
    ans =+ num * 2
    if type(num) is float:
        return round(ans)
    else:
        minOperations(num)
