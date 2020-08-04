import numpy as np
import matplotlib.pyplot as plt
import glob


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)

files = glob.glob("../LOGS/profile*.data")
files.sort()
for name in files:

    age = np.loadtxt(name, skiprows = 2, max_rows = 1, usecols = 4, unpack = True)

    age_string = "%.1e yrs" % (age,)

    T, rho, P, chi_rho, chi_T, cp, Lratio, opacity, grav, vconv = np.loadtxt(name, skiprows = 6, usecols=(3,4,5,9,10,11,12,13,14,15), unpack = True)
    
    T = 10.0**T
    rho = 10.0**rho
    P = 10.0**P
    
    alpha = chi_T / chi_rho  / T

    plt.plot(rho, vconv, lw=1, alpha=1, label = age_string)
    #plt.plot(rho, P / rho / grav, lw=1, alpha=1, label = age_string)
    #plt.plot(rho, alpha * P / rho / cp, lw=1, alpha=1, label = age_string)
    #plt.plot(rho, 10.0**(-Lratio), lw=1, alpha=1, label = age_string)
    #plt.plot(rho, cp, lw=1, alpha=1, label = age_string)
    #plt.plot(rho, grav, lw=1, alpha=1, label = age_string)
    #plt.plot(rho, T, lw=1, alpha=1, label = age_string)
    #plt.plot(rho, alpha, lw=1, alpha=1, label = age_string)
    #plt.plot(rho, alpha * T, lw=1, alpha=1, label = age_string)
 
plt.legend()

ax.set_yscale('log')
ax.set_xscale('log')

ax.tick_params(axis='both', which='major', labelsize=15)
ax.tick_params(axis='both', which='minor', labelsize=15)

#plt.xlim((1e5,5e9))
#plt.ylim((1e-9,1e-4))
plt.xlabel(r'$\rho\ (\mathrm{g\ cm^{-3}})$', fontsize=14)
plt.ylabel(r'$v_\mathrm{conv}\ (\mathrm{cm\ s^{-1}})$', fontsize=14)
#plt.ylabel(r'$H\ (\mathrm{cm})$', fontsize=14)
#plt.ylabel(r'$H/H_T = \alpha gH/c_P$', fontsize=14)
#plt.ylabel(r'$\kappa\ (\mathrm{cm^2\ g^{-1}})$', fontsize=14)
#plt.ylabel(r'$L/L_{\rm rad}$', fontsize=14)
#plt.ylabel(r'$C_P\ (\mathrm{erg\ g^{-1}\ K^{-1}})$', fontsize=14)
#plt.ylabel(r'$g (cm\ s^{-2})$', fontsize=14)
#plt.ylabel(r'$\alpha$', fontsize=14)

#plt.tight_layout()
#plt.show()
#plt.savefig('profile_T.pdf',bbox_inches='tight')
#plt.savefig('profile_alphaT.pdf',bbox_inches='tight')
#plt.savefig('profile_alpha.pdf',bbox_inches='tight')
#plt.savefig('profile_grav.pdf',bbox_inches='tight')
#plt.savefig('profile_Lratio.pdf',bbox_inches='tight')
#plt.savefig('profile_opacity.pdf',bbox_inches='tight')
#plt.savefig('profile_H_over_HT.pdf',bbox_inches='tight')
#plt.savefig('profile_H.pdf',bbox_inches='tight')
plt.savefig('profile_vconv.pdf',bbox_inches='tight')
