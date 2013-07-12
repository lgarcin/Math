'''
Created on 13 juil. 201
@author: Laurent
'''

from math import *

def rectangle1(f,a,b,n):
    h=(b-a)/n
    return sum([f(a+k*h) for k in range(0,n)])*h

def rectangle2(f,a,b,n):
    h=(b-a)/n
    return sum([f(a+k*h) for k in range(1,n+1)])*h

def trapeze(f,a,b,n):
    h=(b-a)/n
    return sum([(f(a+k*h)+f(a+(k+1)*h))/2 for k in range(0,n)])

print(rectangle1(lambda x:cos(x),0,pi,1000))
print(rectangle2(lambda x:cos(x),0,pi,1000))
print(trapeze(lambda x:cos(x),0,pi,1000))
