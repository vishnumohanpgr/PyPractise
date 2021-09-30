"""
Write a program to find out the prime factors of a number. Example: prime factors of 56 --> 2, 2, 2, 7
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


def prime_factors(num):
    try:
        if int(num) <= 0:
            raise
        elif num == 1:
            print("The number '1' cannot have any prime factors!")
        elif prime_check(num) == 1:
            return num
        else:
            i = 2
            while i != (int(num/2)+1):
                if prime_check(i) == 1 and prime_check(num) == 0 and (num % i) == 0:
                    num = int(num / i)
                    print(i)
                    i = 2
                elif prime_check(num) == 1:
                    return num
    except:
        print("Only a whole number will accepted as a valid argument!")


prime_factors(56)

