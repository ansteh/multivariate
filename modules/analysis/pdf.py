import numpy as np

class Pdf():
    def __init__(self, column):
        self.column = column
        self.n = column.size
        self.p, self.x = np.histogram(self.column, bins=self.n)
        #print self.p, self.x

    def probability(self, value):
        if((value < self.x[0]) or (value > self.x[self.n])):
            return 0
        else:
            return self.intigrate(value)

    def intigrate(self, value):
        end = self.getIntegralEndIndex(value)
        start = end-1
        return self.p[start]*(self.x[end]-self.x[start])

    def getIntegralEndIndex(self, value):
        sliced = self.x[np.where(self.x >= value)]
        index = self.n - sliced.size + 1
        #print index, self.x[index], sliced[0]
        return index
