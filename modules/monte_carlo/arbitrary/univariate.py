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
        samples = np.array([])
        for i in range(size):
            u = numpy.random.uniform()
