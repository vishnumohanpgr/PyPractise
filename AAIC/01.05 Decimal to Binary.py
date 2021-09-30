"""
Write a function that converts a decimal number to binary number.
"""


def div2(n):  # Function that uses modulo of 2 to n for every instance of recursion, while returning the results in string format.
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return str(n % 2) + div2(int(n/2))


def deci2bin(num):  # Function that returns the final result of the decimal to binary conversion.
    return div2(int(num))[::-1]  # Result has to be printed in reverse.


print(deci2bin(4.0))
