# Produced by Balram Kandoria for Project Airfoil Optimization
import numpy as np
import math as m
import matplotlib.pyplot as plt
from MSES import MSES
from XFOIL import XFOIL
from scipy import interpolate
import sys



def TEWedgeAng(x,y):

    Xupp, Yupp, Xlow, Ylow = MSES(x,y)
# Interpolate
    f = interpolate.interp1d(Xupp, Yupp, kind='quadratic', fill_value='extrapolate')
    f1 = interpolate.interp1d(Xlow, Ylow, kind='quadratic', fill_value='extrapolate')
    xnew = np.linspace(0,1,120)########################################################################################################
    yinterp_upp = f(xnew)
    yinterp_low = f1(xnew)


    X = np.append(xnew, np.flipud(xnew))
    Y = np.append(yinterp_low, np.flipud(yinterp_upp))

    dydx = np.ones(len(yinterp_upp))
    for i in range(len(dydx)):
        if i != 0:
            dydx[i] = (yinterp_upp[i-1] - yinterp_upp[i])/(xnew[i-1]-xnew[i])
            loc_upp = i

    n = len(yinterp_upp)

    traile_upp_slope = dydx[i-2]

    point_upp = traile_upp_slope * xnew[n-2] + (yinterp_upp[n-1] - traile_upp_slope*xnew[n-1])


    dx_upp = (xnew[i-1]-xnew[i])#(xnew[n-1] - xnew[n-2])
    dy_upp = (yinterp_upp[i-1] - yinterp_upp[i])#(yinterp_upp[n-1] - point_upp)
    Phi_upp = m.atan2(dy_upp,dx_upp)
    if Phi_upp < 0:
        Phi_upp = Phi_upp + (np.pi * 2)
    DELTA_upp = np.deg2rad(np.rad2deg(Phi_upp) + 90)





    dydx = np.ones(len(yinterp_low))
    for i in range(len(dydx)):
        if i != 0:
            dydx[i] = (yinterp_low[i-1] - yinterp_low[i])/(xnew[i-1]-xnew[i])
            loc_low = i

    n = len(yinterp_low)

    traile_low_slope = dydx[i-2]

    point_low = traile_low_slope * xnew[n-2] + (yinterp_low[n-1] - traile_low_slope*xnew[n-1])
    # The normal vector code was taken from source code produced by Josh the Engineer

    dx_low = (xnew[i-1]-xnew[i])#(xnew[n-1] - xnew[n-2])
    dy_low = (yinterp_low[i-1] - yinterp_low[i])#(yinterp_upp[n-1] - point_upp)
    Phi_low = m.atan2(dy_low,dx_low)
    if Phi_low < 0:
        Phi_low = Phi_low + (np.pi * 2)
    DELTA_low = np.deg2rad(np.rad2deg(Phi_low) + 90)






#s = np.linspace(.8, 1, 100)

#Normalx1 = np.zeros(len(s))
#Normaly1 = np.zeros(len(s))
    s = np.sqrt((dx_upp ** 2) + (dy_upp ** 2))

#for i in range(len(s)):
    Normalx1 = [xnew[loc_upp] + .3 * np.cos(Phi_upp),1]
    Normaly1 = [yinterp_upp[loc_upp] + .3 * np.sin(Phi_upp), yinterp_upp[n-1]]
    Normalx2 = [xnew[loc_low] + .3 * np.cos(Phi_low),1]
    Normaly2 = [yinterp_low[loc_low] + .3 * np.sin(Phi_low), yinterp_low[n-1]]

    print(Normalx1)
#f1 = interpolate.interp1d(Normalx1, Normaly1, kind='quadratic', fill_value='extrapolate')
#xnew1 = np.linspace(.8,1,10000)#########################################################################################################
#top_line = f1(xnew1)
    dx_tan_up = Normalx1[0] - Normalx1[1]
    dy_tan_up = Normaly1[0] - Normaly1[1]
    dx_tan_low = Normalx2[0] - Normalx2[1]
    dy_tan_low = Normaly2[0] - Normaly2[1]

    Ang_up = np.rad2deg(m.atan2(dy_tan_up,dx_tan_up))
    Ang_low = np.rad2deg(m.atan2(dy_tan_low, dx_tan_low))

    print(Ang_up)
    print(Ang_low)
    if Ang_up > 0 and Ang_low > 0:
        if Ang_up <= 0:
            Ang_up = Ang_up + 180
        elif Ang_up > 0:
            Ang_up = 180 - Ang_up

        if Ang_low <= 0:
            Ang_low = Ang_low + 180
        elif Ang_low > 0:
            Ang_low = 180 - Ang_low
        p11 = abs(Ang_low - Ang_up)
    else:
        if Ang_up <= 0:
            Ang_up = Ang_up + 180
        elif Ang_up > 0:
            Ang_up = 180 - Ang_up

        if Ang_low <= 0:
            Ang_low = Ang_low + 180
        elif Ang_low > 0:
            Ang_low = 180 - Ang_low
        p11 = abs(Ang_low + Ang_up)

    #
    #
    # plt.scatter(xnew[n-2], point_upp)
    # plt.scatter(xnew[n-1], yinterp_upp[n-1])
    # plt.scatter(xnew[n-2], point_low)
    # plt.scatter(xnew[n-1], yinterp_low[n-1])
    # plt.plot(xnew,yinterp_upp, label = 'Upper Airfoil Surface')
    # plt.plot(xnew,yinterp_low, label = 'Lower Airfoil Surface')
    # plt.plot(Normalx1, Normaly1, label = 'Top Tangent Curve')
    # plt.plot(Normalx2, Normaly2, label = 'Bottom Tangent Curve')
    # plt.fill(X,Y, c = 'k')
    # plt.legend(loc='best')
    # plt.ylim([-.2,.2])
    #
    # plt.show()

    return p11



