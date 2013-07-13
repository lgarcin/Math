'''
Created on 13 juil. 201
@author: Laurent
'''

from math import *
from pylab import *

def rectangle1(f,a,b,n):
    h=(b-a)/n
    return sum([f(a+k*h) for k in range(0,n)])*h

def rectangle2(f,a,b,n):
    h=(b-a)/n
    return sum([f(a+k*h) for k in range(1,n+1)])*h

def trapeze(f,a,b,n):
    h=(b-a)/n
    return sum([(f(a+k*h)+f(a+(k+1)*h))/2 for k in range(0,n)])*h

x=[n for n in range(1,100)]
r1=[abs(rectangle1(cos,0,5*pi/2,n)-1) for n in x]
r2=[abs(rectangle2(cos,0,5*pi/2,n)-1) for n in x]
t=[abs(trapeze(cos,0,5*pi/2,n)-1) for n in x]

plot(x,r1,label="rectangle1")
plot(x,r2,label="rectangle2")
plot(x,t,label="trapèze")
legend()
show()