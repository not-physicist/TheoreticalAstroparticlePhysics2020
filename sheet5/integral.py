import scipy.integrate as integrate
import numpy as np

T0 = 6.626e-4 #eV
Tr = 0.26 #eV
OmegaM = 0.27
OmegaRad = 0
MPl = 1.2e28 #eV
G = 1/MPl**2

def integrand(T):
    return 1/T * (OmegaM * (T/T0)**3 + OmegaRad * (T/T0)**4 )**(-0.5)

I = integrate.quad(integrand, Tr, np.inf)[0]
print("The integral is ", I)

t = 14.4e9 * I
print("The time of last scattering is ", t , " year")
print("-----------------")

gStar = 3.36
OmegaB = 0.046
etaB = 6.2e-10
mP = 0.9e9 #eV

rhoRad = gStar * np.pi**2 /30 * Tr**4
print("rhoRad: ", rhoRad, "eV^4")

nGamma = 2 * 1.2 / np.pi**2 * Tr**3
rhoM = OmegaM/ OmegaB * mP * etaB * nGamma
print("rhoM: ", rhoM, "eV^4")

H = np.sqrt( 8 * np.pi / 3 * G * (rhoM + rhoRad))
print("Hubble parameter: ", H, "eV")
t = 2/3 / H * 1e9 # GeV-1
t *= 6.6e-25 /3.16e7 # year
print("time of last scattering: ", t, "year")
