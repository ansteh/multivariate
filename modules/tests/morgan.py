import pandas as ps
import numpy as np
import os, sys
sys.path.append('../../modules/')

from analysis.correlation import corr
from algorithms.morgan import morgan

#data = ps.read_csv(os.path.join(os.path.dirname(__file__), "../WIKI-FB.csv"), sep = ',')

#C is covariance matrix
def apply(C):
    A = morgan(C)
    #print A
    print C
    print np.dot(A, A.T)
    #print np.subtract(C, np.dot(A, A.T))
    print C == np.dot(A, A.T)
    return A
