"""

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

from math import ceil, sqrt


def prime_check(n):  # Function that checks if n is prime or not.
    if abs(n) == 0 or abs(n) == 1:
        return 0
    elif abs(n) == 2:
        return 1
    else:
        for i in range(2, int(ceil(sqrt(abs(n))) + 1)):
            if n % i == 0:
                return 0
    return 1


def rec_len(n):  # Returns the length of the recurring cycle of n.
    rcl = 1
    remainders = []
    d = 1
    while True:
        if d % n == 0:
            rcl = 0
            break
        elif d in remainders:
            rcl = len(remainders) - remainders.index(d)
            break
        remainders.append(d)
        d = (d * 10) % n
    return rcl


def rec_cycle(lmt):  # Returns the dividend with the longest recurring cycle, within the range lmt.
    result = 1
    rcl = 0
    for i in range(1, lmt):
        if prime_check(i) == 1:
            if rcl < rec_len(i):
                rcl = rec_len(i)
                result = i
    return result


print(rec_cycle(1000))

"""
Notes:
The prime check is a non-essential function & is being used to make the function run faster.

"""