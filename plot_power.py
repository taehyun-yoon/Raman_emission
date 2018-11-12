import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from population import Population
from rabi import Rabi

xvar = 'power'
yvar = 'gamma_R'

detune = -1.0 # [GHz]
d = pd.read_csv("alldata.txt",sep='\t')
d = d[d['Note'] != 'D']
d1 = d[(d['measure_date']==20171110) & (d['Note']=='P')]
d1[xvar] = 1.0e-9 * d1[xvar]

xp = np.linspace(0,6.2e-6,100)

def fitFunc(x, a, b):
  return a*Population().rhosum(detune,x)+b

#fitParams, fitCovariances = curve_fit(fitFunc, Population().rhosum(detune,d1[xvar]), d1[yvar], p0=(0.01,0))
fitParams, fitCovariances = curve_fit(fitFunc, d1[xvar], d1[yvar], p0=(0.01,0))

width = 5.5
ratio = 0.8
fig = plt.figure()
fig.set_size_inches(width, width*ratio)
ax = fig.add_subplot(111)
#pt1_label = '20171120, 620nW'
#plt.errorbar(Population().rhosum(detune,d1[xvar]),d1[yvar],yerr=d1[yvar]*d1['g_std'], fmt='o', capsize=5, label='$\sim$ 5000 atoms, Pump 1.0 GHz')
plt.errorbar(1.0e6*d1[xvar],d1[yvar],yerr=d1[yvar]*d1['g_std'], fmt='o', capsize=5, label='$\sim$5000 atoms, $\Delta$ = -1.0GHz')

plt.plot(1.0e6*xp,fitFunc(xp,fitParams[0],fitParams[1]))
print("slope = {0:.3f}".format(fitParams[0]))
print("intercept = {0:.3f}".format(fitParams[1]))

if 'd2' in dir():
  plt.errorbar(Population().rhosum(detune,d2[xvar]),d2[yvar],xerr=d2[xvar]*d2['num_std'],yerr=d2[yvar]*d2['g_std'], fmt='o', capsize=5, label='Nov. 21, {0}GHz, {1}nW'.format(d2['detune'].unique()[0], d2['power'].unique()[0]))

if 'd3' in dir():
  plt.errorbar(d3[xvar],d3[yvar],xerr=d3[xvar]*d3['num_std'],yerr=d3[yvar]*d3['g_std'], fmt='o', capsize=5, label='Nov. 22, {0}GHz, {1}nW'.format(d3['detune'].unique()[0], d3['power'].unique()[0]))

if 'd4' in dir():
  plt.errorbar(d4[xvar],d4[yvar],xerr=d4[xvar]*d4['num_std'],yerr=d4[yvar]*d4['g_std'], fmt='o', capsize=5, label='Nov. 22, {0}GHz, {1}nW'.format(d4['detune'].unique()[0], d4['power'].unique()[0]))


#plt.errorbar(d1[xvar],d1[yvar],xerr=d1[xvar]*d1['num_std'],yerr=d1[yvar]*d1['g_std'], fmt='o', capsize=5, label='Nov. 21, 2.0GHz, 310nW')

plt.legend(fontsize=16,loc=2)
plt.ylim(0,1.3*max(d1[yvar]))
plt.xlabel('power (uW)', fontsize=18)
#plt.xlabel('$\sum _{F\'=3,4,5} \ \dfrac{\Omega_{F\'}^{2}}{4 \Delta_{F\'}^{2} + 2 \Omega_{F\'}^{2}}$', fontsize=16)
plt.ylabel('$\Gamma_R$/2$\pi$ (kHz)', fontsize=18)
#plt.xticks(np.arange(0.0, 0.7, 0.1),fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
#ax.text(2800,8,'Slope = 17.85 kHz/$\mu$W', fontsize=16)
plt.tight_layout()
plt.savefig('gamma_power.svg')
#plt.show()
