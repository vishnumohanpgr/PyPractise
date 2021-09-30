import datetime


class WriteFile(object):

    def __init__(self, filename, writer):
        self.filename = filename
        self.writer = writer()

    def write(self, data, dlmt):
        fh = open(self.filename, 'a')
        self.writer(fh, data, dlmt)
        fh.close()

class LogWriter(WriteFile):

    def write(self):
        