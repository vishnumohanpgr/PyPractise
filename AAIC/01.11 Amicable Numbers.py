"""
Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal to the other number.
For example 220 and 284 are amicable numbers.
Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284
Sum of proper divisors of 284 = 1+2+4+71+142 = 220
Write a function to print pairs of amicable numbers in a range
"""


def divsum(n):  # Function that returns the sum of the divisors of a given number.
    if abs(int(n)) == 0:
        return 0
    else:
        return sum([i for i in range(1, int(n/2)+1) if n % i == 0])


def amicableRange():  # Function that prints out all pairs of amicable numbers in a given range (st to sp).
    while True:
        try:
            st = abs(int(input("Enter the lower limit(start): ")))
            sp = abs(int(input("Enter the higher limit(stop): ")))
            if st >= sp:
                print("Invalid range! Stop should be greater than start. ")
                continue
            print("Amicable Numbers between {0} & {1}:".format(st, sp))
            for i in range(st, sp):
                if divsum(divsum(i)) == i and divsum(i) != i and (sp > divsum(i) >= st):
                    print(i, ":", divsum(i))
            break
        except ValueError:
            print("Only Whole numbers are accepted as valid range!")
            continue


amicableRange()
