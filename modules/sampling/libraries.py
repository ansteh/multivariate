import numpy as np
import scipy
import math

class Sampling():
    def __init__(self, columnsOptions):
        self.columns = columnsOptions
        # print self.create_integral_func_by("5*x")(0,1)
        # print self.create_integral_func_by("5*x")(-np.inf,1)
        x = -np.inf
        print eval('math.exp(2)')
        print eval('np.exp(-x)')

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
