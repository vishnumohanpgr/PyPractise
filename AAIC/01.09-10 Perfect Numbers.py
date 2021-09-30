"""
Write a function sumPdivisors() that finds the sum of proper divisors of a number.
Proper divisors of a number are those numbers by which the number is divisible, except the number itself.
For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18.

A number is called perfect if the sum of proper divisors of that number is equal to the number.
For example 28 is perfect number, since 1+2+4+7+14=28.
Write a program to print all the perfect numbers in a given range.
"""


def sumPdivisors(num):  # Function that prints out every divisor of a given whole number.
    try:
        if abs(int(num)) == 0:
            print("Zero does not have any proper divisors!")
        else:
            print("Proper divisors of {} are:".format(num))
            for i in range(1, int(num/2)+1):
                if num % i == 0:
                    print(i, end=" ")
    except ValueError:
        print("Only Whole numbers are accepted as valid input!")


def percheck(n):  # Function that checks if a given number is perfect or not.
    if abs(int(n)) == 0:
        return 0
    elif n == sum([i for i in range(1, int(n/2)+1) if n % i == 0]):
        return 1
    else:
        return 0


def perfectRange():
    while True:
        try:
            st = abs(int(input("Enter the lower limit(start): ")))
            sp = abs(int(input("Enter the higher limit(stop): ")))
            if st >= sp:
                print("Invalid range! Stop should be greater than start. ")
                continue
            print("Perfect Numbers between {0} & {1}:".format(st, sp))
            for i in range(st, sp):
                if percheck(i) == 1:
                    print(i, end=" ")
            break
        except ValueError:
            print("Only Whole numbers are accepted as valid range!")
            continue


sumPdivisors(36)
perfectRange()
