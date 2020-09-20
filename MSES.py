# Produced by Balram Kandoria for Project Airfoil Optimization
import numpy as np

def MSES(x,y):
    n = len(x)
    #Yupp = np.ones(n)*300
    #Xupp = np.ones(n)*300
    #Ylow = np.ones(n)*300
    #Xlow = np.ones(n)*300

    dx = np.zeros(len(x))
    for i in range(len(x)):
        if i != 0:
            dx[i] = x[i] - x[i - 1]
            if dx[i] == 0:
                print('Found')
    a = 0
    for i in range(len(x)):
        if a == 0:
            if dx[i] > 0:
                a = 1
                loc = i

    #LDE = x[loc]  # [np.where(dx == min(dx))]
    Xlow = x[loc:n-1]
    Xupp = x[0:loc-1]
    Ylow = y[loc:n-1]
    Yupp = y[0:loc-1]
    #for i in range(n):
    #        if y[i] >= 0:
    #                Yupp[i] = y[i]
     #               Xupp[i] = x[i]
    #for i in range(n):
     #       if y[i] < 0:
    #                Ylow[i] = y[i]
    #                Xlow[i] = x[i]
    #Yupp = np.delete(Yupp, np.where(Yupp == 300))
    #Ylow = np.flipud(np.delete(Ylow, np.where(Ylow == 300)))
    #Xupp = np.delete(Xupp, np.where(Xupp == 300))
    #Xlow = np.flipud(np.delete(Xlow, np.where(Xlow == 300)))
    return Xupp, Yupp, Xlow, Ylow