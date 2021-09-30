"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""


def row_sum_odd_numbers(n):
    return n**3


print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))
"""
NOTES:
Sum of first n odd numbers = n^2
nth odd number = 2n-1
Total number of all elements in the triangle above its nth row = n(n-1)/2
First element of nth row = n(n-1)+1
Last element of nth row = n(n+1)-1

After substitutions & factorisations, we have,
The row-sum of nth row in the triangle = n^3
"""
