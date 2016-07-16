import pandas as ps
import numpy as np

from analysis.correlation import corr
from analysis.covariance import cov
from analysis.symmetric import isSymmetric
from analysis.definite import isPositiveDefinite
from discrete.transformation import test
#from algorithms.morgan import morgan
import tests.morgan as morgan

data = ps.read_csv("resources/WIKI-FB.csv", sep = ',')
#data = ps.read_csv("apple-tree.csv", sep = ',')

matrix = data.as_matrix()
matrix = matrix[:, 1:]
matrix = matrix.T
matrix = np.array(matrix, dtype=np.float64)
#matrix = np.nan_to_num(matrix)

#dim = 5
#matrix = matrix[:dim,:dim]

#print matrix
#print cov(matrix)
#print corr(matrix)

def testMorgan():
    morgan.testbed()

testMorgan()
