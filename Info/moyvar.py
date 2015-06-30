'''
Created on 14 juil. 2013

@author: Laurent
'''

from numpy import random

def moyenne(tab):
    s=0
    for x in tab:
        s+=x
    return s/len(tab)

def variance(tab):
    m=moyenne(tab)
    s=0
    for x in tab:
        s+=(x-m)**2
    return s/len(tab)

def var(tab):
    s=0;
    ss=0;
    for x in tab:
        s+=x
        ss+=x**2
    n=len(tab)
    return ss/n-(s/n)**2

tab=random.randint(1,100,20)
print(tab)
print(moyenne(tab))
print(variance(tab))
print(var(tab))