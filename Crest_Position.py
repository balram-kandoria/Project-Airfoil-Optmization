# Produced by Balram Kandoria for Project Airfoil Optimization
import numpy as np
import math as m
import matplotlib.pyplot as plt
from MSES import MSES
from XFOIL import XFOIL
from scipy import interpolate
import sys


def Crest_Pos(x,y):
    Xupp, Yupp, Xlow, Ylow = MSES(x,y)
    # Interpolate
    plt.plot(Xlow, Ylow)
    plt.plot(Xupp, Yupp)
    plt.show()
    f = interpolate.interp1d(Xupp, Yupp, kind='quadratic', fill_value='extrapolate')
    f1 = interpolate.interp1d(Xlow, Ylow, kind='quadratic', fill_value='extrapolate')
    xnew = np.linspace(0,1,1000)########################################################################################################
    yinterp_upp = f(xnew)
    yinterp_low = f1(xnew)

    camber = (yinterp_upp + yinterp_low)/2


    X = np.append(xnew, np.flipud(xnew))
    Y = np.append(yinterp_low, np.flipud(yinterp_upp))

    dydx = np.ones(len(yinterp_upp))
    for i in range(len(dydx)):
        if i != 0:
            dydx[i] = (yinterp_upp[i] - yinterp_upp[i-1])/(xnew[i]-xnew[i-1])
    a = 0
    for i in range(len(yinterp_upp)):
        if a ==0:
            if dydx[i] < 0:
                a=1
                loc = i


    X_upp_crest_loc = xnew[loc]#[np.where(dydx == min(abs(dydx)))]
    Y_upp_crest_loc = yinterp_upp[loc]#[np.where(dydx == min(abs(dydx)))]
    p2 = X_upp_crest_loc
    p3 = Y_upp_crest_loc

    dydx = np.ones(len(yinterp_low))*-1
    for i in range(len(dydx)):
        if i != 0:
            dydx[i] = (yinterp_low[i] - yinterp_low[i-1])/(xnew[i]-xnew[i-1])
    a = 0
    for i in range(len(yinterp_low)):
        if a ==0:
            if dydx[i] > 0:
                a=1
                loc = i

    X_low_crest_loc = xnew[loc]#[np.where(dydx == min(abs(dydx)))]
    Y_low_crest_loc = yinterp_low[loc]#[np.where(dydx == min(abs(dydx)))]
    p5 = X_low_crest_loc
    p6 = Y_low_crest_loc
    plt.plot(x,y)
    plt.scatter(p5,p6, label = 'Lower Crest Point')
    plt.scatter(p2,p3, label = 'Upper Crest Point')


    return p2, p3, p5, p6

