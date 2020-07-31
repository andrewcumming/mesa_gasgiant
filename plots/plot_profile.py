import numpy as np
import matplotlib.pyplot as plt
import glob


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)


files = glob.glob("LOGS/profile*.data")
files.sort()
for name in files:

    age = np.loadtxt(name, skiprows = 2, max_rows = 1, usecols = 4, unpack = True)

    age_string = "%.1e yrs" % (age,)

    T, rho, chi_rho, chi_T = np.loadtxt(name, skiprows = 6, usecols=(3,4,9,10), unpack = True)
    
    T = 10.0**T
    rho = 10.0**rho
    
    alpha = chi_T / chi_rho  / T
    
#    plt.plot(rho, T, lw=1, alpha=1, label = age_string)
    plt.plot(rho, alpha, lw=1, alpha=1, label = age_string)
#    plt.plot(rho, alpha * T, lw=1, alpha=1, label = age_string)
 
plt.legend()

ax.set_yscale('log')
ax.set_xscale('log')

ax.tick_params(axis='both', which='major', labelsize=15)
ax.tick_params(axis='both', which='minor', labelsize=15)

#plt.xlim((1e5,5e9))
#plt.ylim((1e-9,1e-4))
plt.xlabel(r'$\rho (g\ cm^{-3})$', fontsize=14)
plt.ylabel(r'$\alpha$', fontsize=14)

#plt.tight_layout()
#plt.show()
#plt.savefig('profile_T.pdf',bbox_inches='tight')
#plt.savefig('profile_alphaT.pdf',bbox_inches='tight')
plt.savefig('profile_alpha.pdf',bbox_inches='tight')
