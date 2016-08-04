import matplotlib.pyplot as plt
import pylab
import numpy as np

plt.style.use('ggplot')

import os, sys
sys.path.append('../../modules/')

from analysis.pdf import sample_from

# Make up some random data
#x = np.concatenate([np.random.normal(0, 1, 10000), np.random.normal(4, 1, 10000)])
x = np.random.chisquare(2, 10000)

samples = sample_from(x, 1000)

plt.hist(x, 25, histtype='step', color='red', normed=True, linewidth=1)
plt.hist(samples, 25, histtype='step', color='blue', normed=True, linewidth=1)

plt.show()

pylab.show()
