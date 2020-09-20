# Produced by Balram Kandoria for Project Airfoil Optimization
import numpy as np
import math as m
import matplotlib.pyplot as plt
from MSES import MSES
from XFOIL import XFOIL
from scipy import interpolate
import sys




def TELoc(x, y):
    Xupp, Yupp, Xlow, Ylow = MSES(x,y)
# Interpolate
    f = interpolate.interp1d(Xupp, Yupp, kind='quadratic', fill_value='extrapolate')
    f1 = interpolate.interp1d(Xlow, Ylow, kind='quadratic', fill_value='extrapolate')
    xnew = np.linspace(0,1,120)########################################################################################################
    yinterp_upp = f(xnew)
    yinterp_low = f1(xnew)

    camber = (yinterp_upp + yinterp_low)/2

    n = len(xnew)
    X = np.append(xnew, np.flipud(xnew))
    Y = np.append(yinterp_low, np.flipud(yinterp_upp))
    Z_location = (yinterp_upp[n-1] + yinterp_low[n-1])/2
    p8 = Z_location
    Z_thickness = abs(yinterp_low[n-1]) + abs(yinterp_upp[n-1])
    p9 = Z_thickness



    dydx = np.ones(len(xnew))
    for i in range(len(xnew)):
        if i != 0:
            dydx[i] = (camber[i-1] - camber[i])/(xnew[i-1]-xnew[i])
            loc_low = i

    n = len(camber)

    trail_slope = dydx[i-2]

    point = trail_slope * xnew[n-2] + (yinterp_low[n-1] - trail_slope*xnew[n-1])


    dx = (xnew[i-1]-xnew[i])#(xnew[n-1] - xnew[n-2])
    dy = (camber[i-1] - camber[i])#(yinterp_upp[n-1] - point_upp)
    Phi = m.atan2(dy,dx)
    if Phi < 0:
        Phi = Phi + (np.pi * 2)
    DELTA_low = np.deg2rad(np.rad2deg(Phi) + 90)

    Normalx2 = [xnew[loc_low] + 1 * np.cos(Phi),1]
    Normaly2 = [camber[loc_low] + 1 * np.sin(Phi), camber[n-1]]


    Phi = np.rad2deg(Phi)
    if Phi > 0:
        Phi = 180 - Phi
    if Phi < 0:
        Phi = 180 + Phi

    p10 = Phi
    # plt.scatter(xnew[n-1], Z_location)
    # plt.scatter(xnew[n-1], yinterp_upp[n-1])
    # plt.scatter(xnew[n-1], yinterp_low[n-1])
    # plt.plot(xnew,yinterp_upp, label = 'Upper Airfoil Surface')
    # plt.plot(xnew,yinterp_low, label = 'Lower Airfoil Surface')
    # plt.plot(xnew, camber)
    # plt.plot(Normalx2, Normaly2, label = 'Bottom Tangent Curve')
    # plt.legend(loc='best')
    # plt.ylim([-.2,.2])
    # plt.grid()
    # plt.show()

    return p8, p9, p10