from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
#import gasgiant as gg


#  Make a plot of the different contributions to energy over time to make
#  sure that energy is being conserved


    
def read_burrows():
    t = np.array([])
    L = np.array([])
    for line in open('mxgm5a.001.txt','r'):
        data = line.split()
        t = np.append(t, float(data[1])*1e9)   
        L = np.append(L, float(data[3]))
    return t,L   
    
def read_profile(name,dir='LOGS'):
    count  = 0
    t = np.array([])
    R = np.array([])
    M = np.array([])
    Eint = np.array([])
    L = np.array([])
    Egrav = np.array([])
    Etot = np.array([])
    err = np.array([])
    for line in open(dir+'/'+name+'.data'):
        data = line.split()
        count = count + 1
        if count > 6:
            t = np.append(t,float(data[2]))
            M = np.append(M,float(data[4]))
            R = np.append(R,float(data[39]))
            L = np.append(L,float(data[38]))
            Egrav = np.append(Egrav,float(data[61])/1e43)
            Eint = np.append(Eint,float(data[62])/1e43)
            Etot = np.append(Etot,float(data[60])/1e43)
            err = np.append(err,float(data[63]))
    return t, M, R, L, Eint, Egrav, Etot, err


msol_me = 1.9892e33/5.9764e27
msol_mj = 1.9892e33/1.8986e30
mj = 1.8986e30
me = 5.9764e27
rj = 6.9911e9
Lsun = 3.8418e33
msol = 1.9892e33  # solar mass (g)
rsol = 6.9598e10 # solar radius (cm)
standard_cgrav = 6.67428e-8 

GM2overR = standard_cgrav * msol**2 / rsol

fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(1,1,1)



t, M, R, L, Eint, Egrav, Etot, err = read_profile('history_cool_jupiter','.')
#t, M, R, Erad, Eint, Egrav, Etot, err = read_profile('history','LOGS')

# normalize by GM^2/R -- grav + int should be -(3/7)GM^2/R for a n=3/2 polytrope
#norm = GM2overR * M**2 / R  / 1e43
#Erad = Erad / norm
#Eint = Eint / norm
#Egrav = Egrav / norm
#Etot = Etot / norm

# it would seem that MESA no longer provides the cumulative luminosity as an output, so make our own version here
Erad = np.zeros(len(L))
for i in range(1,len(L)):
    Erad[i] = 3.15e7 * simpson(L[:i+1], t[:i+1]) 
Erad = Erad / 1e43 

#plt.plot(t,-Erad, 'C3', label = r'$-E_{rad}$')
#plt.plot(t,Eint, 'C0--', label = r'$E_i$')
plt.plot(t,Eint+Egrav+Erad, label = r'$E_\mathrm{grav}+E_\mathrm{int}+\int\, L\, dt$')
plt.plot(t,Eint+Egrav, label = r'$E_\mathrm{grav}+E_\mathrm{int}$')
plt.plot(t,Egrav, label = r'$E_\mathrm{grav}$')

#plt.plot(t,(-Erad+Etot[0])*(1.0-err), 'C4--', label = r'Predicted $E_{tot}$')
#plt.plot(t,(Erad[-1]-Erad)+Etot[-1], 'C3--', label = r'Predicted $E_{tot}$')
#plt.plot(t,Eint+Egrav, 'C0:', label = r'$E_i+E_g$')
#plt.plot(t,Etot+Erad, '-', label = r'$E_{tot}+E_{rad}$')


plt.legend()
plt.xlim((1e3,1e10))
#plt.xlim((1e3,3e5))
#plt.ylim((1e-6,1e-4))
plt.ylabel(r'${\rm Energy}\ [10^{43}\ {\rm erg}]$', fontsize=12)

plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)

#ax.set_yscale('log')
ax.set_xscale('log')

plt.xlabel(r'${\rm Time}\ [{\rm yr}]$', fontsize=11)

#plt.tight_layout()
#plt.show()
plt.savefig('energy.pdf',bbox_inches='tight')
