"""
Write a function that inputs a number and prints the multiplication table of that number.
"""


def mul_table_gen():
  while True:
    try:
      num = int(input("Please, enter the number for multiplication-table generation: "))
      for i in range(1, 11):
        print("{} x {} = {}".format(i, num, i*num))
    except:
      print("Please, enter a valid integer!")
      continue
    break


mul_table_gen()
