import scipy.integrate as integrate
import numpy as np

T0 = 6.626e-4 #eV
Tr = 0.26 #eV
OmegaM = 0.27
OmegaRad = 1e-4

def integrand(T):
    return 1/T * (OmegaM * (T/T0)**3 + OmegaRad * (T/T0)**4 )**(-0.5)

I = integrate.quad(integrand, Tr, np.inf)[0]
print("The integral is ", I)

t = 14.4e9 * I
print("The time of last scattering is ", t )
