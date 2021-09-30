"""
Write a function cubesum() that accepts an integer and returns the sum of the cubes of individual digits of that number.
Use this function to make functions PrintArmstrong() and isArmstrong() to print Armstrong numbers
and to find whether is an Armstrong number.
"""


def cubesum(n):  # Function that uses recursion to find the sum of cubes of its individual digits.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return int((n % 10) ** 3) + cubesum(int(n/10))


def isArmstrong():  # Function that checks if any given input is an Armstrong number or not and prints the result.
    while True:
        try:
            num = abs(int(input("Enter the number to be tested as Armstrong: ")))
            if cubesum(num) == num:
                return print("{0} is an Armstrong number.".format(num))
            else:
                return print("{0} is not an Armstrong number.".format(num))
        except ValueError:
            print("Only Whole numbers are accepted as input!")
            continue


def PrintArmstrong():  # Function that prints out all Armstrong numbers between 0 & the given limit.
    while True:
        try:
            lmt = abs(int(input("Enter the limit: ")))
            print("Armstrong Numbers between 0 & {0}:".format(lmt))
            for i in range(lmt + 1):
                if cubesum(i) == i:
                    print(i)
            break
        except ValueError:
            print("Only Whole numbers are accepted as limit!")
            continue


print(cubesum(123))
isArmstrong()
PrintArmstrong()
