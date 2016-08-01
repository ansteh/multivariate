import numpy as np

class Pdf():
    def __init__(self, column):
        self.column = column
        self.n = column.size
        self.p, self.x = np.histogram(self.column, bins=self.n)
        self.bin_width = self.x[1]-self.x[0]
        print self.p, self.x

    def probability(self, a, b=None):
        if(b is None):
            return self.single(a)
        else:
            return self.intigrate(a, b)

    def single(self, value):
        if((value < self.x[0]) or (value > self.x[self.n])):
            return 0
        else:
            return self.intigrate(value)

    def intigrate(self, a, b=None):
        if(b is None):
            index = self.getIntegralEndIndex(a)
            return self.p[index]*self.bin_width
        else:
            # start = self.getIntegralEndIndex(a)
            # end = self.getIntegralEndIndex(b)
            start = self.x[np.where(self.x < a)].size
            end = self.x[np.where(self.x < b)].size
            print start, end
            return self.bin_width * np.sum(self.p[start:end])
            # return self.p[start]*(self.x[end]-self.x[start])


    def getIntegralEndIndex(self, value):
        sliced = self.x[np.where(self.x >= value)]
        index = self.x.size - sliced.size
        if(index > 0):
            index -= 1
        return index
