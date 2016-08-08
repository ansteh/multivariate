import os, sys
sys.path.append('../modules/')
import json

import pandas as pd
import numpy as np

#import matplotlib.pyplot as plt
import pylab
# import seaborn as sns
#
# sns.set(color_codes=True)
# plt.style.use('ggplot')

import generators.collection as generators

generator = generators.find_generator_by_url("generate/numpy/data")
samples = generator.simulate(1000)

print samples
print samples.shape

generator.plot(samples)

pylab.show()
