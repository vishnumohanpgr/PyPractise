"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def letter_count(num):  # Function that counts all the letters in the given num.
    l_dig = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]  # 0 to 19
    m_dig = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]  # 20 to 90
    h_dig = [7, 8, 7, 7, 8, 11]  # 100 to Quadrillion
    ones = num % 10
    tens = (num % 100) // 10
    hundreds = ((num % 1000) - ((tens * 10) + ones)) // 100
    # Getting 10s & 1s sorted.
    if tens <= 1:
        result = l_dig[num % 100]
    elif tens > 1 and ones == 0:
        result = m_dig[tens]
    elif tens > 1:
        result = (m_dig[tens] + l_dig[ones])
    # Getting 100s & above sorted.
    if hundreds != 0 and tens == 0 and ones == 0:
        result = (l_dig[hundreds] + h_dig[0])
    elif hundreds != 0:
        result += (l_dig[hundreds] + h_dig[0] + 3)
    return result


def sum_count(low, high):  # Finds the sum of all letters in the english numbers from low to high (max = 1000).
    count = low
    total = 0
    if high > 1000:
        return print('Higher limit has to be less than 1000')
    elif high == 1000:
        total = 11
        high -= 1
    for i in range(low, high+1):
        total += letter_count(i)
        print(count, total)
        count += 1
    return total


print(sum_count(1, 1000))
