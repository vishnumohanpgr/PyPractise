"""

Joey Greenhorn has a problem with his code. It is not returning the right values. Can you help him fix it?
a = 10
b = 20
a, b = swap(a, b)
print(a, b) # Should print out "20, 10", but "20, 20" gets printed out... HELP!

"""


def swap(a, b):  # Function that swaps the values of a to b & b to a.
    return b, a


print(swap(10, 20))
