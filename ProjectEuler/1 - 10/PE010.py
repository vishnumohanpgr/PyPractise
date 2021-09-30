"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from math import ceil, sqrt


def prime_check(n):  # Function that checks if n is prime or not.
    for i in range(2, int(ceil(sqrt(n)) + 1)):
        if n == 2:
            return 1
        elif n % i == 0:
            return 0
    return 1


print(sum(i for i in range(2, 2000000) if prime_check(i) == 1))
