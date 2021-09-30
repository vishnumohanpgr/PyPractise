"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz_seq_len(n):  # Function that returns the length of collatz sequence starting from n.
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = (n / 2)
        else:
            n = (3 * n) + 1
        count += 1
    return count


def lar_collatz_seq(lmt):  # Returns the starting number within lmt, that yields the largest collatz sequence.
    count = 0
    result = 0
    for i in range(lmt - 1, int((lmt / 2)) + 1, -1):
        if collatz_seq_len(i) > count:
            count = collatz_seq_len(i)
            result = i
    return result


print(lar_collatz_seq(1000000))
