"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


from math import factorial, ceil, sqrt


def div_count(num):  # Function that returns all possible divisors of num.
    count = 1
    for i in range(1, int(ceil(sqrt(num)))):
        if num % i == 0:
            count += 1
            if i != (num / i):
                count += 1
    return count


def tri_num(n):  # Function that prints out the n'th triangular number.
    return int((n * (n + 1)) / 2)


def high_div_tri_num(lmt):  # Function that returns the first triangular number with more than lmt number of divisors.
    for i in range(1, factorial(500)):
        if div_count(tri_num(i)) > lmt:
            return tri_num(i)


print(high_div_tri_num(500))
