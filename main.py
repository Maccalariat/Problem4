"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import cProfile
import time
import itertools
import string


def reverse(strorint):
    return int(str(strorint)[::-1])


def palindrome_range(start,stop,step=1):
    for x in range(start,stop,step):
        if str(x)==str(x)[::-1]:
            yield x


def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True


def main(k):
    # for p in palindrome_range(100000, 999999, 1):
    max_palindrome = 0
    mx = 0
    my = 0
    for x in range(999, 100, -1):
        for y in range(999, 100, -1):
            z = x * y
            if str(z) == str(z)[::-1]:
                if z > max_palindrome:
                    max_palindrome = z
                    mx = x
                    my = y
                    return (max_palindrome, mx, my)


if __name__ == '__main__':
    start_time = time.time()

    print("--- %s seconds ---" % (time.time() - start_time))

    cProfile.run('(m, x, y) = main(6)')
    print("max palindrome = " , m , " from numbers ", x, " , ", y)

    # print(list)

    print("--- %s seconds ---" % (time.time() - start_time))
