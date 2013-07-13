'''
Created on 12 juil. 2013

@author: Laurent
'''
from math import *

def dicho(f,a,b,eps):
    if abs(b-a)<eps:
        return (a+b)/2
    if f(a)*f((a+b)/2)<=0:
        return dicho(f,a,(a+b)/2,eps)
    else:
        return dicho(f,(a+b)/2,b,eps)

def dic(f,a,b,eps):
    while abs(b-a)>=eps:
        if f(a)*f((a+b)/2)<=0:
            b=(a+b)/2
        else:
            a=(a+b)/2
    return (a+b)/2
    
print(dicho(lambda x:cos(x)-x,0.,10.,.00000001))
print(dic(lambda x:cos(x)-x,0.,10.,0.00000001))