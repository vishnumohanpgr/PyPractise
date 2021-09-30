"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
# Note: Middle term of, layers in Pascal's triangle with odd number of digits, will be the number of possible paths.


def pascals_tri_gen(lmt):  # Function that generates middle term of 20th odd line in Pascal's triangle.
    layer = 0.5
    ptri = [1, 1]
    temp = [1]
    while layer < lmt:
        for i in range(1, len(ptri)):
            temp.append(ptri[i - 1] + ptri[i])
        temp.append(1)
        ptri = temp
        temp = [1]
        layer += 0.5
    return ptri[int(len(ptri) / 2)]


print('Maximum possible paths = ', pascals_tri_gen(20))
