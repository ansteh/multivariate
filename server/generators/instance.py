import os, sys
sys.path.append('../../modules/')

import pandas as ps
import numpy as np

from analysis.covariance import cov
from analysis.symmetric import isSymmetric
from analysis.definite import isPositiveDefinite
import generators.fs as fs

import generation.normal as normal
import generation.nonnormal as nonnormal
from sampling.libraries import DatasetGenerator

import schedule, time

def start_thread_of_function(func, seconds):
    def run_schedule():
        while 1:
            try:
                schedule.run_pending()
                # time.sleep(1)
            except:
                time.sleep(5)
                print "error"

class Blueprint():
    def __init__(self, options):
        self.options = options
        self.url = self.options['url']

        if(self.options_include_cache_limit()):
            self.cache_bench = self.options['generator']['data_cache_limit']
        else:
            self.cache_bench = 100000

        self.cache = np.array([])

        self.generator_web_interface = self.options['generator']['web_interface']
        self.listener_web_interface = self.options['listener']['web_interface']

    def options_include_cache_limit(self):
        return 'data_cache_limit' in self.options['generator'].keys()

    def set_callback(self, callback):
        self.callback = callback

    def execute_callback(self, data):
        if(hasattr(self, 'callback')):
            self.callback(data)

    def get_listener_url(self):
        return self.options['listener']['domain']+'/'+self.url

    def get_select_options(self):
        return self.options['listener']['select_options']

    def has_frequence(self):
        return 'frequence' in self.options['generator'].keys()

    def get_frequence_in_seconds(self):
        return self.options['generator']['frequence']['value']

    def simulate(self, size=1, select_options=None):
        return self.produce_data(size, select_options)

    # def produce_and_cache_data():
    #     if(self.cache.size < self.cache_bench):

class Imitator(Blueprint):
    def __init__(self, options):
        Blueprint.__init__(self, options)

        self.threshold = 1e-6
        self.sample = self.get_sample_data()
        self.matrix = self.sample.as_matrix()
        self.matrix = self.matrix.T
        self.matrix = np.array(self.matrix, dtype=np.float64)
        self.C = cov(self.matrix)
        # print self.sample, self.C
        # print 'isSymmetric', isSymmetric(self.C, self.threshold)
        # print normal.simulate(self.matrix, 1000)

    def get_sample_data(self):
        return fs.get_csv_resource(self.options['resource']['csv'])

    def produce_data(self, size=1, select_options=None):
        if(isSymmetric(self.C, self.threshold) and isPositiveDefinite(self.C)):
            data = normal.simulate(self.matrix, size)
        else:
            data = nonnormal.simulate(self.matrix.T, size)

        if(hasattr(self, 'callback')):
            self.callback(data)

        return data

class Numpy_Datagenerator(Blueprint):
    def __init__(self, options):
        Blueprint.__init__(self, options)

        self.columnOptions = self.options['resource']['columns']
        self.generator = DatasetGenerator(self.columnOptions)

    def produce_data(self, size=1, select_options=None):
        data = self.generator.rvs(size)

        if(hasattr(self, 'callback')):
            self.callback(data)

        return data

def create(options):
    if('columns' in options['resource'].keys()):
        return Numpy_Datagenerator(options)
    return Imitator(options)
