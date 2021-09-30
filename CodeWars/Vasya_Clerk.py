"""

The new "Avengers" movie has just been released!
There are a lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and,
give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment.
Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change
(you can't make two bills of 25 from one of 50)

"""


def tickets(people):
    db25, db50 = 0, 0
    for pay in people:
        if pay == 25:                   # When paying with a 25 dollar bill.
            db25 += 1
        elif pay == 50:                 # When paying with a 50 dollar bill.
            if db25 >= 1:
                db25 -= 1
                db50 += 1
            else:
                return "NO"
        elif pay == 100:                # When paying with a 100 dollar bill.
            if db50 >= 1 and db25 >= 1:
                db50 -= 1
                db25 -= 1
            elif db25 >= 3:
                db25 -= 3
            else:
                return "NO"
    return "YES"


print(tickets([]))
print(tickets([25, 25]))
print(tickets([25, 25, 50, 100]))
print(tickets([50, 25, 25, 50, 100]))

"""
Notes: Solution using a dictionary.

def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0
    
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
        
  return 'YES'

"""