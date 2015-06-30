# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 08:51:28 2015

@author: Laurent
"""

from sympy.ntheory import mobius

def nbptsfixes(perm):
    s=0
    for i in range(len(perm)):
        if perm[i]==i:
            s+=1
    return s

def nbc(perm,k):
    p=list(perm)
    s=0
    for i in range(1,k+1):
        if k%i==0:
            s+=nbptsfixes(p)*mobius(k//i)
        for j in range(len(perm)):
            p[j]=perm[p[j]]
    return s//k


