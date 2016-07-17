import pandas as ps
import numpy as np
import os, sys
sys.path.append('../../modules/')

import generation.normal as generator
import analysis.deviation as deviation
from analysis.covariance import cov
from analysis.correlation import corr
from analysis.mean import mean

def getNormalDistrubutedData():
    data = ps.read_csv(os.path.join(os.path.dirname(__file__), "../resources/apple-tree.csv"), sep = ',')
    matrix = data.as_matrix()
    matrix = matrix.T
    matrix = np.array(matrix, dtype=np.float64)
    return matrix

def testNormalDistributedGenerator():
    matrix = getNormalDistrubutedData()
    simulated = generator.simulate(matrix, 1000000)
    #print simulated
    threshold = 1e-02
    print deviation.conforms(mean(matrix), mean(simulated.T), threshold)
    print deviation.conforms(cov(matrix), cov(simulated.T), 1e-01)
    print deviation.disparity(cov(matrix), cov(simulated.T))