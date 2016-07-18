import pandas as ps
import numpy as np
import os, sys
sys.path.append('../../modules/')

from analysis.covariance import cov
from analysis.correlation import corr
from analysis.mean import mean
from algorithms.morgan import morgan

def simulate(data, factors=0, maxtrials=5, multiplier=1, seed=0):
    n = len(data)
    dim = len(data[0])
    simulated = np.zeros((n,dim))
    distribution = np.zeros((n,dim))
    iteration = 0
    RMSR = 1
    trialsWithoutImprovement = 0

    #apply distribution from supplied data
    distribution = simulated.copy()
    targetCorr = corr(data.T)
    intermidiateCorr = targetCorr.copy()
    #print data.shape
    #print simulated.shape
    #print targetCorr, targetCorr.shape

    if(factors == 0):
        eigvalsObserved = np.linalg.eigvals(intermidiateCorr)
        eigvalsRandom = np.zeros((100,dim))
        randomData = np.zeros((n,dim))

        for i in range(0, 100):
            for j in range(0, dim):
                randomData[:, j] = np.random.shuffle(distribution[:, j])
            eigvalsRandom[i, :] = np.linalg.eigvals(corr(randomData.T))
