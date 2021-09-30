"""

Usually when you buy something, you're asked whether your credit card number,
phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"

"""


def maskify(cc):
    if len(cc) < 4:
        return cc
    else:
        result = ""
        for i in range(len(cc)- 1, -1, -1):
            if (len(cc) - i) <= 4:
                result += cc[i]
            else:
                result += '#'
        cc = result[::-1]
    return cc


print(maskify(""))
print(maskify("123"))
print(maskify("SF$SDfgsd2eA"))
"""
NOTES:
Optimal Solution: 
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
"""