import os, sys
sys.path.append('../modules/')

import pandas as ps
import numpy as np

import generation

class Generator():
    def __init__(self, options):
        self.options = options

    # def fit(self, X):
    #     U = np.unique(X)
    #     I = range(len(U))
    #
    #     self.forward = {key: value for key, value in zip(U, I)}
    #
    # def onehot(self, idx, max):
    #     z = np.zeros(max)
    #     z[idx] = 1.0
    #     return z
    #
    # def transform(self,X):
    #     result = [ self.onehot( self.forward[x], len(self.forward)) for x in X]
    #     return np.array(result)
