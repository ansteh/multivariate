import pandas as ps
import numpy as np

from analysis.correlation import corr
from analysis.covariance import cov
from discrete.transformation import test
#from algorithms.morgan import morgan
import tests.morgan as morgan

data = ps.read_csv("WIKI-FB.csv", sep = ',')
#df = ps.DataFrame(data)
#print data.corr()
#print np.nan_to_num(np.array([[np.nan, np.nan], [np.nan, np.nan]], dtype=np.float64))

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
    C = cov(matrix)
    morgan.apply(C)

testMorgan()
