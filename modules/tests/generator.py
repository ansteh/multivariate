import pandas as ps
import numpy as np
import os, sys
sys.path.append('../../modules/')

import generation.normal as generator
import generation.nonnormal as nonnormalGenerator
import analysis.deviation as deviation
from analysis.covariance import cov
from analysis.correlation import corr
from analysis.mean import mean
import algorithms.fleishman_multivariate as fm

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

def getNonNormalDistrubutedData():
    data = ps.read_csv(os.path.join(os.path.dirname(__file__), "../resources/WIKI-FB.csv"), sep = ',')
    matrix = data.as_matrix()
    matrix = matrix[:, 1:]
    matrix = np.array(matrix, dtype=np.float64)
    return matrix

def testNonNormalDistributedGenerator():
    data = getNonNormalDistrubutedData()
    simulated = nonnormalGenerator.simulate(data)
    print simulated.shape
    print corr(data) - corr(simulated)
    return simulated

def testFleishmanGenerator():
    data = getNormalDistrubutedData()
    Sample = fm.sample_from_matrix(data)
    print Sample
