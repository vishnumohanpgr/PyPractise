"""
Write a program to implement these formulae of permutations and combinations.
Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!
"""


def fact(n):
  if n in {0, 1}:
    return 1
  else:
    return n * fact(n - 1)


def permu_comb():  # Function that takes values for n & r and, prints out their permutation & combination results.
    while True:
        try:
            n = int(input("Enter the number of objects (n): "))
            r = int(input("Enter the number of places/selections (r): "))
            if (int(r) or int(n)) < 0:
                raise ValueError
            elif r > n:
                print("Sorry, value of r cannot be greater than n.")
                continue
            else:
                print("Number of permutations of {0} objects taken {1} at a time: p({0}, {1}) = {2}".format(n, r, int(fact(n)/fact(n-r))))
                print("Number of combinations of {0} objects taken {1} at a time is: c({0}, {1}) = {2}".format(n, r, int((fact(n)/fact(n-r))/fact(r))))
        except ValueError:
            print("Please, enter positive-integer values for both n and r!!")
            continue
        break


permu_comb()
