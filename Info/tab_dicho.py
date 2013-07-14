'''
Created on 13 juil. 2013

@author: Laurent
'''

from numpy import random
def dicho(tab,val,a=None,b=None):
    if a==None:
        a=0
    if b==None:
        b=len(tab)-1
    if a>=b:
        return None
    c=(a+b)//2
    if tab[c]==val:
        return c
    elif tab[c]>val:
        return dicho(tab,val,a,c-1)
    else:
        return dicho(tab,val,c+1,b)
    
def dic(tab,val):
    a=0
    b=len(tab)-1
    c=(a+b)//2
    while(tab[c]!=val and a<b):
        if(tab[c]>val):
            b=c-1
        else:
            a=c+1
        c=(a+b)//2
    if a>=b:
        return None
    else:
        return c

tab=sorted(random.randint(1,100,20))
val=random.randint(1,100)
print(val,tab)
print(dicho(tab,val))
print(dic(tab,val))
