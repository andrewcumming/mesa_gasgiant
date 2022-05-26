import numpy as np
import matplotlib.pyplot as plt
import glob


def plotone(name):

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1,1,1)

    ylabel = ''

    files = glob.glob("../LOGS/profile*.data")
    files.sort()
    for filename in files:

        age = np.loadtxt(filename, skiprows = 2, max_rows = 1, usecols = 4, unpack = True)

        if age < 1e3:
            continue

        age_string = "%.1e yrs" % (age,)

        T, rho, P, chi_rho, chi_T, cp, Lratio, opacity, grav, vconv, csound = np.loadtxt(filename, skiprows = 6, usecols=(3,4,5,9,10,11,12,13,14,15,16), unpack = True)

        T = 10.0**T
        rho = 10.0**rho
        P = 10.0**P

        alpha = chi_T / chi_rho  / T

        if name == 'T':
            plt.plot(rho, T, lw=1, alpha=1, label = age_string)
            ylabel = r'$T\ (\mathrm{K})$'            
        if name == 'opacity':
            plt.plot(rho, opacity, lw=1, alpha=1, label = age_string)    
            ylabel = r'$\kappa\ (\mathrm{cm^2\ g^{-1}})$'
        if name == 'alphaT':
            plt.plot(rho, alpha * T, lw=1, alpha=1, label = age_string)
            ylabel = r'$\alpha T$'    
        if name == 'alpha':
            plt.plot(rho, alpha, lw=1, alpha=1, label = age_string)
            ylabel = r'$\alpha$'
        if name == 'grav':
            plt.plot(rho, grav, lw=1, alpha=1, label = age_string)
            ylabel = r'$g (cm\ s^{-2})$'
        if name == 'Lratio':
            plt.plot(rho, 10.0**(-Lratio), lw=1, alpha=1, label = age_string)
            ylabel = r'$L/L_{\rm rad}$'
        if name == 'H_over_HT':
            plt.plot(rho, alpha * P / rho / cp, lw=1, alpha=1, label = age_string)
            ylabel = r'$H/H_T = \alpha gH/c_P$'
        if name == 'H':
            plt.plot(rho, P / rho / grav, lw=1, alpha=1, label = age_string)
            ylabel = r'$H\ (\mathrm{cm})$'
        if name == 'vconv':
            plt.plot(rho, vconv, lw=1, alpha=1, label = age_string)
            ylabel = r'$v_\mathrm{conv}\ (\mathrm{cm\ s^{-1}})$'
        if name == 'csound':
            plt.plot(rho, csound, lw=1, alpha=1, label = age_string)
            ylabel = r'$c_s\ (\mathrm{cm\ s^{-1}})$'
        if name == 'mach':
            plt.plot(rho, vconv/csound, lw=1, alpha=1, label = age_string)
            ylabel = r'$v_\mathrm{conv}/c_s$'
        if name == 'cp':
            plt.plot(rho, cp, lw=1, alpha=1, label = age_string)
            ylabel = r'$C_P\ (\mathrm{erg\ g^{-1}\ K^{-1}})$'

    plt.legend()

    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.tick_params(axis='both', which='minor', labelsize=15)

    #plt.xlim((1e5,5e9))
    #plt.ylim((1e-9,1e-4))
    plt.xlabel(r'$\rho\ (\mathrm{g\ cm^{-3}})$', fontsize=14)
    plt.ylabel(ylabel, fontsize=14)

    #plt.tight_layout()
    #plt.show()
    if name == 'T':
        plt.savefig('profile_T.pdf',bbox_inches='tight')
    if name == 'opacity':
        plt.savefig('profile_opacity.pdf',bbox_inches='tight')
    if name == 'alphaT':
        plt.savefig('profile_alphaT.pdf',bbox_inches='tight')
    if name == 'alpha':
        plt.savefig('profile_alpha.pdf',bbox_inches='tight')
    if name == 'grav':
        plt.savefig('profile_grav.pdf',bbox_inches='tight')
    if name == 'Lratio':
        plt.savefig('profile_Lratio.pdf',bbox_inches='tight')
    if name == 'H_over_HT':
        plt.savefig('profile_H_over_HT.pdf',bbox_inches='tight')
    if name == 'H':
        plt.savefig('profile_H.pdf',bbox_inches='tight')
    if name == 'vconv':
        plt.savefig('profile_vconv.pdf',bbox_inches='tight')
    if name == 'csound':
        plt.savefig('profile_csound.pdf',bbox_inches='tight')
    if name == 'mach':
        plt.savefig('profile_mach.pdf',bbox_inches='tight')
    if name == 'cp':
        plt.savefig('profile_cp.pdf',bbox_inches='tight')

    plt.close()

names = ['T', 'opacity', 'alphaT', 'alpha', 'grav', 'Lratio','H_over_HT','H','vconv','csound','mach','cp']

for name in names:
    plotone(name)
    




