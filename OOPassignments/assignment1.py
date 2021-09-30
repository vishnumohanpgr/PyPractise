class MaxSizeList(object):

    def __init__(self, lmt):  # Validating lmt as integer & instance's empty-list as lst.
        try:
            self.lmt = int(lmt)
            self.lst = []

        except ValueError:
            print('Invalid entry! ')

    def push(self, x):  # Function that appends x into instance's list & pops elements when necessary, with respect to lmt
        while len(self.lst) >= self.lmt:
            self.lst.pop(0)
        self.lst.append(x)

    def get_list(self):
        return self.lst
