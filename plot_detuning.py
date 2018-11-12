import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from population import Population

xvar = 'detune'
yvar = 'gamma_R'


P = 620e-9 # Raman pump power [W]
d = pd.read_csv("alldata.txt",sep='\t')
d = d[d['Note'] != 'P']
d0 = d[(d['measure_date']==20171110) & (d['power']==int(P*1.0e9))]
d0 = d0[d0['detune'] < -0.35]
d1 = d0[d0['wait'] == 60]
d2 = d0[d0['wait'] == 30]
d3 = d[(d['measure_date']==20171116) & (d['power']==int(P*1.0e9))]
d3 = d3[d3['detune'] < -0.35]
xp = np.linspace(-3.1,-0.37, 100)

def fitFunc(x, a, b):
    return a*Population().rhosum(x, P)+b

#fitParams, fitCovariances = curve_fit(fitFunc, Population().rhosum(d2[xvar], P), d2[yvar], p0=(0.01,0))
fitParams, fitCovariances = curve_fit(fitFunc, pd.concat([d1,d2,d3])[xvar], pd.concat([d1,d2,d3])[yvar], p0=(0.01,0))

width = 5.5 
ratio = 0.8
fig = plt.figure()
fig.set_size_inches(width, width*ratio)
ax = fig.add_subplot(111)

plt.errorbar(d1[xvar],d1[yvar],yerr=d1[yvar]*d1['g_std'], fmt='o', capsize=5, label='{0}nW, n~1000'.format(d1['power'].unique()[0]))
#plt.errorbar(Population().rhosum(d1[xvar],P),d1[yvar],yerr=d1[yvar]*d1['g_std'], fmt='o', capsize=5, label='{0}nW, n~1000'.format(d1['power'].unique()[0]))
#plt.semilogy(1/(d1[xvar]**2+Omega**2),d1[yvar], linestyle='', marker='o', label='{0}nW, n~1000'.format(d1['power'].unique()[0]))

if 'd2' in dir():
   plt.errorbar(d2[xvar],d2[yvar],yerr=d2[yvar]*d2['g_std'], fmt='o', capsize=5, label='{0}nW, n~5000'.format(d2['power'].unique()[0]))
#    plt.errorbar(Population().rhosum(d2[xvar],P),d2[yvar],yerr=d2[yvar]*d2['g_std'], fmt='o', capsize=5, label='{0}nW, n~5000'.format(d2['power'].unique()[0]))
#  plt.semilogy(1/(d2[xvar]**2+Omega**2),d2[yvar], linestyle='', marker='^', label='{0}nW, n~5000'.format(d1['power'].unique()[0]))

if 'd3' in dir():
   plt.errorbar(d3[xvar],d3[yvar],yerr=d3[yvar]*d3['g_std'], fmt='o', capsize=5, label='{0}nW, n~9000'.format(d3['power'].unique()[0]))
#    plt.errorbar(Population().rhosum(d3[xvar],P),d3[yvar],yerr=d3[yvar]*d3['g_std'], fmt='o', capsize=5, label='{0}nW, n~9000'.format(d3['power'].unique()[0]))
#  plt.semilogy(1/(d3[xvar]**2+Omega**2),d3[yvar], linestyle='', marker='*', label='{0}nW, n~9000'.format(d1['power'].unique()[0]))

plt.plot(xp,fitParams[0]*Population().rhosum(xp, P) + fitParams[1])

print("slope = {0:.3f}".format(fitParams[0]))
print("intercept = {0:.3f}".format(fitParams[1]))

plt.legend(fontsize=16)
#plt.ylim(0,1.2*max(d2[yvar]))
plt.xlabel('detuning (GHz)', fontsize=18)
#plt.xlabel('$\sum _{F\'=3,4,5} \ \dfrac{\Omega_{F\'}^{2}}{4 \Delta_{F\'}^{2} + 2 \Omega_{F\'}^{2}}$', fontsize=16)
plt.ylabel('$\Gamma_R$/2$\pi$ (kHz)', fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
#ax.text(3500,8,'Slope = 17.85kHz/$\mu$W', fontsize=16)
plt.tight_layout()
plt.savefig('gamma_detuning.svg')
#plt.show()
