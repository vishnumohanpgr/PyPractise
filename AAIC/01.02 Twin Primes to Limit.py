"""
Write a program to print twin primes less than 1000.
If two consecutive odd numbers are both prime then they are known as twin primes.
"""

from math import ceil, sqrt


def prime_check(n):  # Function that checks if n is prime or not.
    if n == 0 or abs(n) == 1:
        return 0
    elif abs(n) == 2:   # Since two is a prime number.
        return 1
    else:
        for i in range(2, int(ceil(sqrt(abs(n))) + 1)):  # Square-root based limit helps improve efficiency of the loop.
            if n % i == 0:
                return 0
    return 1


def twin_prime(lmt):    # Function that returns all possible twin-primes within the given lmt.
    try:
        if int(lmt) < 0:
            raise
        for i in range(1, lmt, 2):  # Staring from 1 & incrementing with 2, to keep things odd.
            if (prime_check(i) and prime_check(i+2)) == 1:
                print("{}:{}".format(i, i+2))
    except:
        print("Limit should be a valid natural number!")


twin_prime(1000)
