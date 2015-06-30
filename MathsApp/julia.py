# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:19:48 2015

@author: Laurent
"""

from numpy import linspace
from matplotlib.pyplot import contour


def P(z):
    return z**4+z

def escape(P,z0,N):
    z=z0
    R=3**(1/3)
    for i in range(N):
        if(abs(z))>R:
            return i
        z=P(z)
    return N
