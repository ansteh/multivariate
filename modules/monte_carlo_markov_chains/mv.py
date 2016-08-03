import pymc as pm
import numpy as np
import numpy.random as rand
#import pdfs
import time

import numpy as np
from numpy.linalg import inv
import pymc as pm

start_time = time.time()

k = 5
rand.seed(1)
true_std = rand.randn(k)
true_mean = rand.randn(k)
true_cov = np.eye(k) * np.outer(true_std, true_std)
n = 100

np.random.seed(1)
vals = np.random.multivariate_normal(true_mean, true_cov, n)

# Trying to give tau a vague prior and reasonable starting value...
tau = pm.Wishart('tau', n=k + 1, Tau=np.eye(k), value=inv(np.eye(k)*10.0))
m = pm.Normal('m', mu=0, tau=1e-5, value=np.zeros(k), size=k)

data = pm.MvNormal('data', m, tau, value=vals, observed=True)

# def logp(value=None, mu=None, tau=None):
#     # Call the GPU function-- which need a covariance matrix
#     return pdfs.mvnpdf(value, [mu], [inv(tau)]).sum()
# data._logp.fun = logp

S = pm.MCMC(locals())
S.sample(iter=1000,burn=0,thin=1)
print 'elapsed time:', time.time() - start_time
#pm.Matplot.plot(S)
