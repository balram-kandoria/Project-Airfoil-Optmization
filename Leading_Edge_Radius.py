# Produced by Balram Kandoria for Project Airfoil Optimization
import numpy as np
import math as m
import matplotlib.pyplot as plt
from MSES import MSES
from XFOIL import XFOIL
from scipy import interpolate
import sys


def LDER(x, y, flagAirfoil, NACA):
    Xupp, Yupp, Xlow, Ylow = MSES(x,y)
    # Interpolate
    plt.plot(Xlow, Ylow)
    plt.plot(Xupp, Yupp)
    plt.show()
    f = interpolate.interp1d(Xupp, Yupp, kind='quadratic', fill_value='extrapolate')
    f1 = interpolate.interp1d(Xlow, Ylow, kind='quadratic', fill_value='extrapolate')
    xnew = np.linspace(0,1,10000)########################################################################################################
    yinterp_upp = f(xnew)
    yinterp_low = f1(xnew)

    camber = (yinterp_upp + yinterp_low)/2



    X = np.append(xnew, np.flipud(xnew))
    Y = np.append(yinterp_low, np.flipud(yinterp_upp))

    radius_diff_up = np.zeros(len(x))
    radius_diff_low = np.zeros(len(x))

    dx = np.zeros(len(X))
    for i in range(len(X)):
        if i != 0:
            dx[i] = X[i] - X[i - 1]
            if dx[i] == 0:
                print('found')

    a = 0
    for i in range(len(X)):
        if a == 0:
            if dx[i] > 0:
                a = 1
                loc = i

    LDE = X[loc]#[np.where(dx == min(dx))]

    i = 10

    P1_forwardx = X[loc + i]
    P1_backwardx = X[loc + (i-1)]
    P2_forwardx = X[loc - i]
    P2_backwardx = X[loc - (i+1)]

    P1_forwardy = Y[loc + i]
    P1_backwardy = Y[loc + (i-1)]
    P2_forwardy = Y[loc - i]
    P2_backwardy = Y[loc - (i+1)]

    dx1 = (P1_forwardx - P1_backwardx)
    dy1 = (P1_forwardy - P1_backwardy)
    Phi1 = m.atan2(dy1,dx1)
    if Phi1 < 0:
        Phi1 = Phi1 + (np.pi * 2)
    DELTA1 = np.deg2rad(np.rad2deg(Phi1) + 90)

    dx2 = (P2_forwardx - P2_backwardx)
    dy2 = (P2_forwardy - P2_backwardy)
    Phi2 = m.atan2(dy2,dx2)
    if Phi2 < 0:
        Phi2 = Phi2 + (np.pi * 2)
    DELTA2 = np.deg2rad(np.rad2deg(Phi2) + 90)

    Xca1 = (P1_forwardx + P1_backwardx)/2
    Xca2 = (P2_forwardx + P2_backwardx)/2

    Yca1 = (P1_forwardy + P1_backwardy)/2
    Yca2 = (P2_forwardy + P2_backwardy)/2


    s = np.linspace(0, .2, 100000)
    # The normal vector code was taken from source code produced by Josh the Engineer
    Normalx1 = np.zeros(len(s))
    Normaly1 = np.zeros(len(s))
    Normalx2 = np.zeros(len(s))
    Normaly2 = np.zeros(len(s))

    for i in range(len(s)):
        Normalx1[i] = Xca1 + s[i] * np.cos(DELTA1)
        Normaly1[i] = Yca1 + s[i] * np.sin(DELTA1)
        Normalx2[i] = Xca2 + s[i] * np.cos(DELTA2)
        Normaly2[i] = Yca2 + s[i] * np.sin(DELTA2)

    f1 = interpolate.interp1d(Normalx1, Normaly1, kind='quadratic', fill_value='extrapolate')
    xnew1 = np.linspace(0,.2,1000)#########################################################################################################
    top_line = f1(xnew1)
    f = interpolate.interp1d(Normalx2, Normaly2, kind='quadratic', fill_value='extrapolate')
    bottom_line = f(xnew1)

#######################################################################################Need Fix########################################################################
    dy = np.zeros(len(xnew1))
    # Find the center of the nose circle
    for i in range(len(xnew1)):
        dy[i] = (abs(top_line[i]) + abs(bottom_line[i]))/2

    loc_centerx = xnew1[np.where(dy == min(abs(dy)))]#dy[loc-1])]
    loc_centery = top_line[np.where(dy == min(abs(dy)))]#dy[loc-1])]


# Radius Calculation
    r = np.sqrt((Xca1 - loc_centerx)**2 + (Yca1 - loc_centery)**2)

########################################################################################################################################################################
#http://www.aerospaceweb.org/question/airfoils/q0173.shtml

    LERP = 1.03
    r_theo = LERP * (.12**2)
    r_error = r - r_theo


# #Create the Nose Circle
#     theta = np.linspace(0, 2*np.pi, 100)
#     circx = (np.cos(theta) * r) + loc_centerx
#     circy = (np.sin(theta) * r) + loc_centery
#     plt.plot(xnew,yinterp_upp, label = 'Upper Airfoil Surface')
#     plt.plot(xnew,yinterp_low, label = 'Lower Airfoil Surface')
#     plt.scatter(P2_backwardx, P2_backwardy)
#     plt.scatter(P2_forwardx, P2_forwardy)
#     plt.scatter(Xca2,Yca2)
#     plt.plot(xnew1, bottom_line, label = 'Bottom Normal Curve')
#
#     plt.scatter(P1_backwardx, P1_backwardy)
#     plt.scatter(P1_forwardx, P1_forwardy)
#     plt.scatter(Xca1,Yca1)
#     plt.plot(xnew1, top_line, label = 'Top Normal Curve')
#
#     plt.fill(X,Y, c = 'k')
#
#     plt.scatter(loc_centerx, loc_centery, label='Center of Nose Circle')
#     plt.plot(circx, circy, label = 'Nose Circle')
#     plt.plot(xnew, camber, label = 'Camber')
#     plt.ylabel('Non-Dimensional Height')
#     plt.xlabel('Non-Dimensional Length')
#     if flagAirfoil[0] == 1:
#         a = 'NACA'
#     plt.title('{} {}'.format(a, NACA))
#     plt.ylim([-.15,.15])
# #plt.xlim([0,.05])
#     plt.legend(loc = 'best')
# #plt.grid()
#     plt.show()
#
    p1 = r
#     print('\n')
#     print('\n')
#     print('\n')
#     print('\n')
#     print('\n')
#
# ####################################################################### NEEDS TO BE ADDRESSED ###############################################################
#     print('line 161 needs a special function to define the thickness of the airfoil for now it is being manually inputted')
# #############################################################################################################################################################
#
#     print('\n')
#     print('\n')

    return p1

