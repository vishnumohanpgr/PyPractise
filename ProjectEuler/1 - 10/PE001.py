"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples_3_5(lmt):  # Function that finds the sum of all multiples of 3 or 5 to the lmt.
    return sum([i for i in range(lmt) if div_by_3_5(i)])


def div_by_3_5(chk):  # Function that checks, if chk is divisible by 3 or 5
    return chk % 3 == 0 or chk % 5 == 0


print(sum_of_multiples_3_5(10))
