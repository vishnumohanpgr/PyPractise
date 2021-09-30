"""
Write a function prodDigits() that inputs a number and returns the product of digits of that number.

If all digits of a number n are multiplied by each other repeating with the product,
the one digit number obtained at last is called the multiplicative digital root of n.
The number of times digits need to be multiplied to reach one digit is called
the multiplicative persistence of n.

Example: 86 -> 48 -> 32 -> 6 (MDR 6, MPersistence 3)
 341 -> 12->2 (MDR 2, MPersistence 2)

Using the function prodDigits() of previous exercise write functions MDR() and
MPersistence() that input a number and return its multiplicative digital root and
multiplicative persistence respectively
"""


def prodDigits(n):
    temp = 1
    for i in str(n):
        temp *= int(i)
    return temp


def MDR(num):  # Function that takes a number as argument & prints out its multiplicative digital root.
    while len(str(num)) > 1:
        num = prodDigits(num)
    return print("Multiplicative Digital Root (MDR): {}".format(num))


def MPersistence(num):  # Function that takes a number as argument & prints out its multiplicative persistence.
    cnt = 0
    while len(str(num)) > 1:
        num = prodDigits(num)
        cnt += 1
    return print("Multiplicative Persistence: {}".format(cnt))


MDR(86)
MPersistence(86)
