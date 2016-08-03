import pymc
import mcmc

M = pymc.MCMC(mcmc, db='pickle')
M.sample(iter=10000, burn=5000, thin=2)
#pymc.Matplot.plot(S)
print M.d.summary()
