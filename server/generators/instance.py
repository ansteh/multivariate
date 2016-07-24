import os, sys
sys.path.append('../modules/')

import pandas as ps
import numpy as np

from analysis.covariance import cov
from analysis.symmetric import isSymmetric
from analysis.definite import isPositiveDefinite
import generators.fs as fs

import generation

class Generator():
    def __init__(self, options):
        self.threshold = 1e-6
        self.options = options
        self.url = self.options['url']
        self.sample = self.get_sample_data()
        self.matrix = self.sample.as_matrix()
        self.matrix = self.matrix.T
        self.matrix = np.array(self.matrix, dtype=np.float64)
        self.C = cov(self.matrix)
        print self.sample, self.C

    def get_sample_data(self):
        return fs.get_csv_resource(self.options['resource']['csv'])


    def simulate(self):
        if(isSymmetric(self.C, self.threshold) and isPositiveDefinite(self.C)):
            return generation.normal.simulate(self.matrix, 1000)
        else:
            return generation.nonnormal.simulate(self.matrix.T, 1000)
    #threshold = 1e-6
    #print 'symmetric:', isSymmetric(C, threshold)
    #print 'positive definite:', isPositiveDefinite(C)
