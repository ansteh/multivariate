import numpy as np
import scipy
import math
import scipy.stats as stats
from analysis.pdf import estimate_pdf
from analysis.pdf import Pdf

class Sampling():
    def __init__(self, columnsOptions):
        self.columns = columnsOptions
        # print self.create_integral_func_by("5*x")(0,1)
        # print self.create_integral_func_by("5*x")(-np.inf,1)
        # x = -np.inf
        # print eval('math.exp(2)')
        # print eval('np.exp(-x)')

    def execute(self, column, size=1):
        if(column.has_key('numpy')):
            return self.sampleColumnByModule('numpy', column, size)
        if(column.has_key('stats')):
            return self.sampleColumnByModule('stats', column, size)
        if(column.has_key('arbitrary_pdf')):
            self.sample_arbitrary_pdf(column['arbitrary_pdf'], size)
            return np.random.uniform(-1, 0, size)

    def sampleColumnByModule(self, moduleName, column, size=1):
        function = column[moduleName]['function']
        parameters =  column[moduleName]['parameters']
        parameters['size'] = size

        if(moduleName == 'numpy'):
            module = np.random

        if(moduleName == 'stats'):
            module = scipy.stats

        return getattr(module, function)(**parameters)

    def generate(self, size=1):
        data = []
        map(lambda column: data.append(self.execute(column, size)), self.columns)
        return np.array(data)

    def sample_arbitrary_pdf(self, pdfFuncStr, size=1):
        sampler = IntegralSimulation(pdfFuncStr)

    def create_integral_func_by(self, funcStr):
        return lambda a, b: scipy.integrate.quad(lambda x: eval(funcStr), a, b)[0]

class IntegralSimulation():
    def __init__(self, pdfFuncStr):
        self.code = pdfFuncStr
        self.func = lambda a, b: scipy.integrate.quad(lambda x: eval(self.code), a, b)[0]
        self.tail = self.func(-np.inf,0)

        for index, x in np.ndenumerate(np.random.uniform(1,0,1000)):
            print x, self.intigrate_cmf(x)

    def intigrate_cmf(self, x):
        if(x>=0):
            return self.tail + self.func(0,x)
        else:
            return self.tail - self.func(x,0)

class Metropolis():

    def sample(self, size=1):
        samples = np.zeros(size)

        last = self.rvs(1)

        for i in range(size):
            u = np.random.uniform()
            x = self.rvs(1)

            if(u < min(1, self.pdf(x) / self.pdf(last))):
                last = x
            samples[i] = last

        return samples

class Metropolis_Scipy_Random(Metropolis):
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.function = getattr(stats, self.name)
        self.pdf = lambda x: self.function.pdf(x, **parameters)
        self.rvs = lambda size: self.function.rvs(size=size, **parameters)

class Metropolis_Numpy_Random(Metropolis):
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.function = getattr(np.random, self.name)
        self.pdf_estimator = Pdf(self.rvs(10000))

    def rvs(self, size=1):
        return self.function(size=size, **self.parameters)

    def pdf(self, x):
        return self.pdf_estimator.probability(x)

class Metropolis_Mixture_Representation(Metropolis):
    def __init__(self, columnOptions):
        self.options = columnOptions
        self.p_of_mixtures = map(lambda options: options['mixture_p'], self.options)
        self.p_of_mixtures = np.array(self.p_of_mixtures)
        self.mixtures = map(lambda options: self.create_metropolis_module(options), self.options)

    def create_metropolis_module(self, representation):
        if(representation['module'] == 'numpy'):
            return Metropolis_Numpy_Random(representation['function'], representation['parameters'])
        if(representation['module'] == 'scipy'):
            return Metropolis_Scipy_Random(representation['function'], representation['parameters'])

    def rvs(self, size=1):
        return np.sum(map(lambda mixture: mixture.rvs(1), self.mixtures))

    def pdf(self, x):
        pdfs = map(lambda mixture: mixture.pdf(x), self.mixtures)
        return np.sum(self.p_of_mixtures * pdfs)

# class Metropolis_Columns():
#     def __init__(self, columnsOptions):
