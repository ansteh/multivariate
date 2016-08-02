import pandas as ps
import numpy as np
import os, sys
sys.path.append('../../../modules/')

import numpy as np
from analysis.pdf import Pdf
from sampling.arbitrary import Sampling

class Metropolis():
    def __init__(self, column):
        self.column = column
        self.pdf = Pdf(self.column)
        self.sampler = Sampling(column)
        self.n = self.column.size

    def sample(self, size=1):
        samples = np.zeros(size)
        last = self.sampler.next()

        for i in range(size):
            u = np.random.uniform()
            x = self.sampler.next()
            #print self.pdf.probability(x) / self.pdf.probability(last)
            #print (self.pdf.probability(x)*self.pdf.probability(last, x)) / (self.pdf.probability(last)*self.pdf.probability(x, last))
            # if(len(samples) > 1):
            #     a = (self.pdf.probability(x)*self.pdf.probability(last, samples[len(samples)-2])) / (self.pdf.probability(last)*self.pdf.probability(samples[len(samples)-2], last))
            # else:
            #     a = self.pdf.probability(x) / self.pdf.probability(last)
            # print a

            if(u < min(1, self.pdf.probability(x) / self.pdf.probability(last))):
                last = x
            samples[i] = last

        return samples
