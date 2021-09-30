"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


from math import factorial, ceil, sqrt


def prime_check(n):  # Function that checks if n is prime or not.
    for i in range(2, int(ceil(sqrt(n)) + 1)):
        if n % i == 0:
            return 0
    return 1


def n_prime(lmt):  # Function that gives the n^th prime number.
    c = 1
    for i in range(3, factorial(lmt), 1):
        if prime_check(i) == 1:
            c += 1
            if c == lmt:
                return i


#print(n_prime(10001))
print(prime_check(13))
