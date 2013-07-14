'''
Created on 12 juil. 2013

@author: Laurent
'''
from math import *

def dicho(f,a,b,eps):
    c=(a+b)/2
    if abs(b-a)<eps:
        return c
    if f(a)*f(c)<=0:
        return dicho(f,a,c,eps)
    else:
        return dicho(f,c,b,eps)

def dic(f,a,b,eps):
    c=(a+b)/2
    while abs(b-a)>=eps:
        if f(a)*f(c)<=0:
            b=c
        else:
            a=c
    return c
    
print(dicho(lambda x:cos(x)-x,0.,10.,.00000001))
print(dic(lambda x:cos(x)-x,0.,10.,0.00000001))