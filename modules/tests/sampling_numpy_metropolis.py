import pandas as ps
import numpy as np
import scipy
import os, sys
import json

sys.path.append('../../modules/')

from sampling.libraries import Metropolis_Numpy_Random as Metropolis_Numpy
from sampling.libraries import Metropolis_Mixture_Representation
def load():
    with open("../resources/sampling_numpy.json") as json_file:
        return json.load(json_file)


normNumpySampler = Metropolis_Numpy('uniform', { 'low': 0, 'high': 1 })
N = 1000
print np.random.uniform(0, 1, N).shape
sample = normNumpySampler.sample(N)
print 'unique', np.unique(sample).size, 'of ', N, np.unique(np.random.uniform(0, 1, N)).size
std_true = scipy.stats.uniform.std(loc=0, scale=1)
std_sampled = np.std(sample)
print std_true, std_sampled, abs(std_true - std_sampled)
mean_sampled = np.mean(sample)
mean_true = scipy.stats.uniform.mean(loc=0, scale=1)
print mean_true, mean_sampled, abs(mean_true - mean_sampled)

Metropolis_Mixture_Representation
print 'Metropolis_Mixture_Representation:'
mixture = Metropolis_Mixture_Representation(load()['columns'][0]['mixture_representation'])
samples = mixture.sample(N)
print 'samples:', samples.shape, 'unique', np.unique(samples).size #, samples
std_true = 0.7*scipy.stats.norm.std(loc=0, scale=1)+0.3*scipy.stats.beta.std(1, 3, scale=1, loc=0)
std_sampled = np.std(samples)
print 'std:', std_true, std_sampled, abs(std_true - std_sampled)
mean_sampled = np.mean(samples)
mean_true = 0.7*scipy.stats.norm.mean(loc=0, scale=1)+0.3*scipy.stats.beta.mean(1, 3, scale=1, loc=0)
print 'mean:', mean_true, mean_sampled, abs(mean_true - mean_sampled)
