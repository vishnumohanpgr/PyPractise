import abc
import datetime


class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def wrt(self, data):
        pass

    def __init__(self, filename):
        self.filename = filename

    def wrtline(self, data):
        fh = open(self.filename, 'a')
        fh.write(data + '\n')
        fh.close()


class DeLimFile(WriteFile):

    def __init__(self, filelname, dlmt):
        super(DeLimFile, self).__init__(filelname)
        self.dlmt = dlmt

    def wrt(self, listdata):
        for i in range(len(listdata)):
            if self.dlmt in listdata[i]:
                listdata[i] = ('"%s"' % listdata[i])
        self.wrtline(self.dlmt.join(listdata))


class LogFile(WriteFile):

    def wrt(self, data):
        self.wrtline('%s    %s' % (datetime.datetime.now().strftime('%H:%M %D-%m-%Y'), data))
