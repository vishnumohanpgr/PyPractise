"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


from math import sqrt


def spl_pytha_triplet(lmt):  # Function that returns the pythagorean triplet who's sum is lmt, if it exists.
    for a in range(2, lmt):
        for b in range(a+1, lmt):
            if (sqrt((a ** 2) + (b ** 2)) % 1) == 0 and int(a + b + (sqrt((a ** 2) + (b ** 2)))) == lmt:
                return a * b * (int(sqrt((a ** 2) + (b ** 2))))
    print("Does not exist!")


print(spl_pytha_triplet(1001))
