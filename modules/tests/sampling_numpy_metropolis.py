import pandas as ps
import numpy as np
import scipy
import os, sys
sys.path.append('../../modules/')

from sampling.libraries import Metropolis_Numpy_Random as Metropolis_Numpy

normNumpySampler = Metropolis_Numpy('uniform', { 'low': 0, 'high': 1 })
sample = normNumpySampler.sample(1000)

print scipy.stats.uniform.std(loc=0, scale=1), np.std(sample)
