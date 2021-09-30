"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_square_diff(lmt):  #
    sum_sq = 0
    sq_sum = 0
    for i in range(1, lmt+1):
        sq_sum += i
        sum_sq += (i ** 2)
    return (sq_sum ** 2) - sum_sq


print(sum_square_diff(100))
