"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


# The smallest multiple has to be a multiple of the product of all the prime numbers within that range.
from math import factorial


def product_prime(low, up):  # Product of all the prime numbers with in a range.
    temp = 1
    for i in range(low, up + 1, 1):
        if prime_check(i) == 1:
            temp *= i
    return temp


def prime_check(n):  # Function that checks if n is prime or not.
    for i in range(2, n):
        if n == 2:
            return 1
        elif n % i == 0:
            return 0
    return 1


def smallest_multiple(low, up):  # Smallest number perfectly divisible by all numbers with in the range.
    inc = product_prime(low, up)
    for x in range(inc, factorial(up) + 1, inc):
        y = up
        while y >= low:
            if x % y == 0 and y == low:
                return x
            elif x % y == 0:
                y -= 1
            else:
                break


print(smallest_multiple(1, 20))
