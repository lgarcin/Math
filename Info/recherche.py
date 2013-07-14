'''
Created on 14 juil. 2013

@author: Laurent
'''

from numpy import random

def recherche(tab,val):
    for idx,x in enumerate(tab):
        if val==x:
            return idx
    return None

def recherche_max(tab):
    if len(tab)==0:
        return None,None
    imaxi=0
    maxi=tab[0]
    for idx,x in enumerate(tab):
        if maxi<x:
            maxi=x
            imaxi=idx
    return maxi,imaxi

tab=random.randint(1,100,20)
val=random.randint(1,100)
print(val,tab)
print(recherche(tab,val))
print(recherche_max(tab))