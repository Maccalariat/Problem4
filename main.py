"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import cProfile
import time
from itertools import permutations

import string


def main(k):
    # for p in palindrome_range(100000, 999999, 1):
    max_palindrome = 0
    mx = 0
    my = 0
    start = 999
    llim =  100
    for x in range(start, llim, -1):
        for y in range(start, llim, -1):
            z = x * y
            if z <= max_palindrome:
                break
            elif str(z) == str(z)[::-1]:
                if z > max_palindrome:
                    max_palindrome = z
                    mx = x
                    my = y
                    start = x-1
                    break

    return max_palindrome, mx, my


if __name__ == '__main__':
    start_time = time.time()

    print("--- %s seconds ---" % (time.time() - start_time))

    cProfile.run('(m, x, y) = main(6)')
    print("max palindrome = " , m , " from numbers ", x, " , ", y)

    # print(list)

    print("--- %s seconds ---" % (time.time() - start_time))
