"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import ceil, sqrt


def pf_gen(lmt):  # Function that generates the largest prime factor of lmt and returns it as lpf.
    lpf = 0
    for i in range(1, lmt+1):
        if lmt % i == 0 and prime_check(i) == 1:
            lpf = i
            lmt = lmt / lpf
        if lmt < lpf:
            break
    return lpf


def prime_check(n):  # Function that checks if n is prime or not.
    if n == 0 or abs(n) == 1:
        return 0
    elif abs(n) == 2:
        return 1
    else:
        for i in range(2, int(ceil(sqrt(abs(n))) + 1)):
            if n % i == 0:
                return 0
    return 1


print(pf_gen(600851475143))
