import json
import pandas as ps
import numpy as np
import os, sys
import schedule, time

sys.path.append('../../modules/')

def load():
    with open("../resources/sampling_numpy.json") as json_file:
        return json.load(json_file)

from sampling.libraries import Sampling

options = load()
columns = options['columns']
sampler = Sampling(columns)

def sample():
    print sampler.execute(sampler.columns[0])

schedule.every(1).seconds.do(sample)

while True:
    schedule.run_pending()
    time.sleep(1)
