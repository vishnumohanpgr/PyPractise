"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
"""


# Function that returns, the 13th letter, after the passed letter.
def nextletter(letter):
    letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    if letter in letters:
        return letters[(letters.index(letter) + 26) % 52]
    else:
        return letter


# Function that ciphers the message into ROT13 format.
def rot13(message):
    result = ''
    for item in message:
        result += nextletter(item)
    return result


print(rot13('Apple13 zZMm'))
