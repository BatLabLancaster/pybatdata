import sys
import numpy as np
from scipy.special import logsumexp
from matplotlib import pyplot as plt
import emcee
from astropy.visualization import hist

def lnprior(theta):
    m, b, Pb, Yb, Vb = theta
    if (-10 < m < 10) and (-500 < b < 500) and (0 < Pb < 1) and (-100 < Yb < 2000) and (0 < np.log(Vb) < 20):
        return 0.0
    else:
        return -np.inf

def lnGau(model, y, var):
    residual = (y - model)**2
    return -0.5 * (np.log(2 * np.pi * var) + residual / var)

def lnprob(theta, x, y, sy):
    lp = lnprior(theta)
    if not np.isfinite(lp):
        # if the params are outside the prior range return -inf
        return -np.inf
    m, b, Pb, Yb, Vb = theta
    # probability of the data points in the line model
    lnpf = lnGau(m * x + b, y, sy**2)
    # probability of the data points in the outlier model
    lnpb = lnGau(Yb, y, Vb + sy**2)
    # combine both probabilities with the propper coefficients and sum them up
    lnlike = logsumexp([lnpf, lnpb], b=[[1 - Pb], [Pb]], axis=0).sum()
    return lp + lnlike

def check_outlier(theta, x, y, sy):
    m, b, Pb, Yb, Vb = theta
    lp = lnprior(theta)
    # probability of the data points in the line model (with the prior)
    lnpf = lnGau(m * x + b, y, sy**2) + np.log(1 - Pb) + lp
    # probability of the data points in the outlier model (with the prior)
    lnpb = lnGau(Yb, y, Vb + sy**2) + np.log(Pb) + lp
    return (lnpb > lnpf)

if len(sys.argv) > 1:
    infile = sys.argv[1]
else:
    sys.exit('STOP To run this program: $ python fit_mcmc.py file.csv')

print('This program assumes the first 2 columns of the file are x,y')
x,y=np.loadtxt(infile,delimiter=',',unpack=True)

# No errors given, so assumed to be ones
val = 1e-6
sy = np.ones(shape=(len(x))) ; sy.fill(val)
print('WARNING: assuming the errors to be {}'.format(val))

print('1. Showing the input data')
plt.figure(1)
plt.errorbar(
    x,
    y,
    sy,
    ls='None',
    mfc='k',
    mec='k',
    ms=5,
    marker='s',
    ecolor='k'
)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0, 700)
plt.show()

# number of parameters being fit
ndim = 5
# number of walkers to use (should be > 2*ndim)
nwalkers = 100
# good starting point
p0 = np.array([1, 240, 0.1, 420, 100])
# start each walker in a small ball around this position
pos = [p0 + 1e-4 * np.random.randn(5) for i in range(nwalkers)]

sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, y, sy))
sampler.run_mcmc(pos, 1000)

print('2. Check the convergance of the MCMC')
plt.figure(2, figsize=(8, 8))
plt.subplot2grid((3, 2), (0, 0))
plt.plot(sampler.chain[:, :, 0].T, alpha=0.05, color='k')
plt.ylabel(r'$m$')
plt.xlabel('step')
plt.subplot2grid((3, 2), (0, 1))
plt.plot(sampler.chain[:, :, 1].T, alpha=0.05, color='k')
plt.ylabel(r'$b$')
plt.xlabel('step')
plt.subplot2grid((3, 2), (1, 0))
plt.plot(sampler.chain[:, :, 2].T, alpha=0.05, color='k')
plt.ylabel(r'$P_b$')
plt.xlabel('step')
plt.subplot2grid((3, 2), (1, 1))
plt.plot(sampler.chain[:, :, 3].T, alpha=0.05, color='k')
plt.ylabel(r'$Y_b$')
plt.xlabel('step')
plt.subplot2grid((3, 2), (2, 0))
plt.plot(np.log(sampler.chain[:, :, 4].T), alpha=0.05, color='k')
plt.ylabel(r'$\ln{(V_b)}$')
plt.xlabel('step')
plt.tight_layout()
plt.show()

# sampler.chain has shape [nwalkers, nsteps, ndim]
samples = sampler.chain[:, 400:, :].reshape((-1, ndim))
fits = np.percentile(samples, [16, 50, 84], axis=0)
fits_pm = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]), zip(*fits))
print(list(fits_pm))

print('3. Showing the marginalised posterior probabilities')
plt.figure(3)
plt.hexbin(samples[:, 0], samples[:, 1], gridsize=100, mincnt=1, cmap='Greys', extent=[2, 2.6, -40, 90])
plt.xlabel(r'$m$')
plt.ylabel(r'$b$')

print('4. Showing the fully marginalised distributions')
plt.figure(4, figsize=(8, 5))
plt.subplot2grid((1, 2), (0, 0))
values, bins, patches = hist(
    samples[:, 0],
    bins='knuth',
    histtype='step',
    color='k',
    density=True,
    lw=1.5
)
plt.xlabel(r'$m$')
plt.ylabel(r'$P(m)$')
plt.subplot2grid((1, 2), (0, 1))
values, bins, patches = hist(
    samples[:, 1],
    bins='knuth',
    histtype='step',
    color='k',
    density=True,
    lw=1.5
)
plt.xlabel(r'$b$')
plt.ylabel(r'$P(b)$')
plt.tight_layout()
plt.show()

print('5. Showing the fraction of outliers')
plt.figure(5, figsize=(6, 5))
# use astropy's hist function so it can pick optimal bin sizes
values, bins, patches = hist(
    samples[:, 2],
    bins='knuth',
    histtype='step',
    color='k',
    density=True,
    lw=1.5
)
plt.xlabel(r'$P_b$')
plt.ylabel(r'$P(P_b)$')
plt.tight_layout()
plt.show()


print('5. Showing the fraction of outliers')
X = np.linspace(0, 300, 500)
# pick 40 random parameter sets from the final sample
idx = np.random.randint(samples.shape[0], size=40)
# plot the data
plt.figure(6)
plt.errorbar(
    x,
    y,
    sy,
    ls='None',
    mfc='k',
    mec='k',
    ms=5,
    marker='s',
    ecolor='k'
)

print('6. Plot the data, best fit and outliers')
# plot the data
plt.figure(7)
plt.errorbar(
    x,
    y,
    sy,
    ls='None',
    mfc='k',
    mec='k',
    ms=5,
    marker='s',
    ecolor='k'
)
# plot the best fit line
plt.plot(X, fits[1][0] * X + fits[1][1], color='k')
# plot a sample of best fit lines
for i in idx:
    f = samples[i]
    plt.plot(X, f[0] * X + f[1], color='k', alpha=0.1)
# get the outliers
q_sample = np.array([check_outlier(sample, x, y, sy) for sample in samples])
q_mask = np.median(q_sample, axis=0).astype(bool)
plt.plot(x[q_mask], y[q_mask], 'o', mfc='none', mec='r', ms=20, mew=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0, 700)
plt.show()

print('Best fit (y=mx+b):')
print('m = {}, b = {}'.format(fits[1][0],fits[1][1]))
plt.savefig('fit.pdf')
