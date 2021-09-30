"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""


def to_camel_case(txt):
    result = ""
    flag = 0
    for i in range(len(txt)):
        if txt[i] == "_" or txt[i] == "-":
            if i != 0:
                flag = 1
        else:
            if flag == 1:
                result += txt[i].capitalize()
                flag = 0
            else:
                result += txt[i]
                flag = 0
    return result


print(to_camel_case("_one--2-_three__four_Five"))

