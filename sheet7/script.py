import numpy as np

MPl = 1.2e19 #GeV
TNS = 80 #keV
Cn = 1.2
G_F = 1.17e-5 #GeV-2

# 2 a)
gStar = 2 + 7/8 * 3 *2 *(4/11)**(4/3)
print("g_* = ", gStar)

MPlStar = MPl / 1.66 / np.sqrt(gStar)
tNS = MPlStar /2 / (TNS*1e-6)**2 # GeV
tNS *= 6.6e-25 #s
print("t_NS = ", tNS, " s")

# 2 b)
Tn = (MPlStar * Cn * G_F**2) ** (-1/3)
Tn *= 1e3
print("Tn = ", Tn, "MeV")

