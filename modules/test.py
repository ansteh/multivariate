import pandas as ps
import numpy as np
from analysis.correlation import corr
from analysis.covariance import cov
from discrete.transformation import test

data = ps.read_csv("WIKI-FB.csv", sep = ',')
#df = ps.DataFrame(data)
#print data.corr()

matrix = data.as_matrix()
matrix = matrix[:, 1:]
matrix = matrix.T
matrix = np.array(matrix, dtype=np.float64)
matrix = np.nan_to_num(matrix)

print matrix
print cov(matrix)
print corr(matrix)
