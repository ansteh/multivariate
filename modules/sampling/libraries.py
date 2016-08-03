import numpy as np
import scipy.stats as stats

class Sampling():
    def __init__(self, columnsOptions):
        self.columns = columnsOptions

    def execute(self, column):
        if(column.has_key('numpy')):
            return self.sampleColumnByModule('numpy', column)
        if(column.has_key('stats')):
            return self.sampleColumnByModule('stats', column)

    def sampleColumnByModule(self, moduleName, column):
        function = column[moduleName]['function']
        parameters =  column[moduleName]['parameters']
        return getattr(np.random, function)(**parameters)
