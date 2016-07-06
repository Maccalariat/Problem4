"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import cProfile
import time
import itertools
import string


def reverse(strorint):
    return int(str(strorint)[::-1])

def generate_palindrome(k):
    return [x for x in itertools.permutations(string.digits, k) if x == x[::-1]]

def main(k):
    list = generate_palindrome(k)


if __name__ == '__main__':
    start_time = time.time()

    print("--- %s seconds ---" % (time.time() - start_time))

    cProfile.run('list = main(6)')
    print(list)
    print("--- %s seconds ---" % (time.time() - start_time))