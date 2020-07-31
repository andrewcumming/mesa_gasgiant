from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
    
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
    mconv = np.array([])
    mdot = np.array([])
    mass = np.array([])
    R = np.array([])
    L = np.array([])
    P0 = np.array([])
    T0 = np.array([])
    try:
         for line in open(dir+'/'+name+'.data'):
             data = line.split()
             count = count + 1
             if count > 6:
                 t = np.append(t, float(data[1]))
                 mconv = np.append(mconv,float(data[6]))
                 mdot = np.append(mdot,10.0**float(data[54]) * msol_me)
                 mass = np.append(mass,float(data[2]) * msol_mj)
                 L = np.append(L,float(data[32]))#*Lsun)
                 R = np.append(R,float(data[34])/rj)
                 P0 = np.append(P0,10.0**float(data[36]))
                 T0 = np.append(T0,10.0**float(data[37]))
         return t, mconv, mdot, R, mass, P0, T0, L
    except:
         return (-1,), (-1,), (-1,), (-1,), (-1,), (-1,), (-1,), (-1,)


def Lfac(t, normalizeL):
    # multiply luminosity by this factor so that we can plot L x t or just L
    if normalizeL:
        return np.array(t)/1e6     # multiply L by t for normalized plot
    else:
        return np.ones(len(t))




def plot_one(normalizeL):

    # Either plot L vs t or (L x t) vs t
    # Set normalizeL = True to multiply by t

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1,1,1)


    if 1:
         t, L = read_burrows()
         L = L * Lfac(t, normalizeL)
         plt.plot(t,L,'k-.', lw=1, alpha=1, label = r'Burrows')

         t, mconv, mdot, R, mass, P0, T0, L = read_profile('history_cool_jupiter', dir='.')
         L = L * Lfac(t, normalizeL)
         plt.plot(t, L, 'k', lw=1, label = r'MESA')
     
         plt.legend()


    #t, mconv, mdot, R, mass, P0, T0, L = read_profile('history', dir='LOGS')
    #L = L * Lfac(t, normalizeL)
    #plt.plot(t, L, 'b', lw=2)


    # ---- finish the plot
    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.tick_params(axis='both', which='minor', labelsize=15)

    # To see the entire history
    plt.xlim((1e5,5e9))

    if normalizeL == False:
        plt.ylim((1e-9,1e-4))
        plt.ylabel(r'$L\,[L_\odot]$', fontsize=14)
    else:    # use this scale for the normalized version
        plt.ylim((3e-6,3e-5))
        plt.ylabel(r'$L\,(L_\odot)\times (t/{\rm Myr})$', fontsize=14)
    plt.xlabel(r'${\rm Time\ since\ formation\ }[{\rm yr}]$', fontsize=14)

    #plt.tight_layout()
    #plt.show()

    if normalizeL == False:
        plt.savefig('lum.pdf',bbox_inches='tight')
    else:
        plt.savefig('lum_normalized.pdf',bbox_inches='tight')



msol_me = 1.9892e33/5.9764e27
msol_mj = 1.9892e33/1.8986e30
rj = 6.9911e9
Lsun = 3.8418e33

# Make two plots: one is the cooling curve L vs t
# the other is L x t vs t, since we expect roughly L propto 1/t
plot_one(True)
plot_one(False)

# In the first plot, we compare with the Burrows et al. cooling curve
# mxgm5a.001.txt
# https://www.astro.princeton.edu/~burrows/
