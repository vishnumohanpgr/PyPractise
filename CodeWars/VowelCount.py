"""

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""


def get_count(input_str):  # Function returns the count of vowels in input_str.
    return sum(1 for i in input_str if i in "aAeEiIoOuU")


print(get_count("Eating Apples."))

"""
Notes:
The use of the expression generator with sum, makes it possible to reduce the no. of lines of code.

"""