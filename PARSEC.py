# Produced by Balram Kandoria for Project Airfoil Optimization
#Reference: P. Vecchia, E. Daniele, E. D'Amato An airfoil shape optimization technique coupling PARSEC parameterization and
# evolutionary algorithm. Elsevier https://www.researchgate.net/publication/259145134_An_airfoil_shape_optimization_technique_coupling_PARSEC_parameterization_and_evolutionary_algorithm Aerospace Science and Technology
# 32 (2014) 103-110

import numpy as np


def PARSEC(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
    

    Cup = [[1 , 1, 1, 1, 1, 1] ,

       [p2 ** (1/2), p2 ** (3/2), p2 ** (5/2), p2 ** (7/2), p2 ** (9/2), p2 ** (11/2)] ,

       [(1/2), (3/2), (5/2), (7/2), (9/2), (11/2)] ,

       [(1/2) * p2 ** (-1/2), (3/2) * p2 ** (1/2), (5/2) * p2 ** (5/2), (7/2) * p2 ** (5/2), (9/2) * p2 ** (7/2), (11/2) * p2 ** (9/2)] ,

       [(-1/4) * p2 ** (-3/2), (3/4) * p2 ** (-1/2), (15/4) * p2 ** (1/2), (15/4) * p2 ** (1/2), (63/4) * p2 ** (5/2), (99/4) * p2 ** (7/2)] ,

       [1, 0, 0, 0, 0, 0]]


    Clo = [[1, 1, 1, 1, 1, 1],

       [p5 ** (1 / 2), p5 ** (3 / 2), p5 ** (5 / 2), p5 ** (7 / 2), p5 ** (9 / 2), p5 ** (11 / 2)],

       [(1 / 2), (3 / 2), (5 / 2), (7 / 2), (9 / 2), (11 / 2)],

       [(1 / 2) * p5 ** (-1 / 2), (3 / 2) * p5 ** (1 / 2), (5 / 2) * p5 ** (5 / 2), (7 / 2) * p5 ** (5 / 2),
        (9 / 2) * p5 ** (7 / 2), (11 / 2) * p5 ** (9 / 2)],

       [(-1 / 4) * p5 ** (-3 / 2), (3 / 4) * p5 ** (-1 / 2), (15 / 4) * p5 ** (1 / 2), (15 / 4) * p5 ** (1 / 2),
        (63 / 4) * p5 ** (5 / 2), (99 / 4) * p5 ** (7 / 2)],

       [1, 0, 0, 0, 0, 0]]

    bup = [ p8 + (p9/2), p3, np.tan(p10 - (p11/2)), 0, p4, np.sqrt(2 * p1)]

    blo = [ p8 - (p9/2), p6, np.tan(p10 + (p11/2)), 0, p7, -np.sqrt(2 * p1)]





    return bup, blo, Clo, Cup