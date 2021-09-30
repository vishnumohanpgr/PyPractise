"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


from math import ceil


def list_palindromes_to_limit(lmt):  # Returns the largest palindrome who's a product of two lmt digit numbers.
    for i in range(int(2 * lmt * '9'), 10 ** ((lmt * 2) - 1), -1):
        if palindrome_checker(i) == 1 and factors(i, lmt) == 1:
            return i
    return 0


def palindrome_checker(n):  # Checks if n is a palindrome.
    rev = ""
    for i in str(n):
        rev = i + rev
    if rev == str(n):
        return 1
    return 0


def factors(p, d):  # Checks if p has 2 factors with d digits.
    for i in range(ceil(p ** 0.5), 10 ** (d - 1), -1):
        if p % i == 0 and p % (p / i) == 0 and len(str(int(p / i))) == d:
            return 1
    return 0


print(list_palindromes_to_limit(3))
