import numpy as np

print("At graviton decoupling:")
g_b = 1 * 1 + 1 * 8 *2 + 2* 3 + 1 *3 + 1*2
print(g_b)

g_f = 3 * 2 * 6 + 3 * 2 + 3 * 1
print(g_f)

gStarsDec =  g_b + 2 * 7 / 8 * g_f
print(gStarsDec)

print("Now:")
gStarsNow = 1 * 2 + 7/8 * 6 * (4/11)
print(gStarsNow)

print("g/g", gStarsNow/gStarsDec)
T_G0 = 2.7 * (gStarsNow/gStarsDec)**(1/3)
print(T_G0)

n_G0 = 1 * 1.2 / np.pi**2 * T_G0**3 # in kelvin^3
n_G0 *= 8.6e-14 ** 3 #GeV^3
n_G0 *= 1.3e41 #cm^-3
print(n_G0)
