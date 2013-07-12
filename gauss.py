'''
Created on 23 juin 2013

@author: Laurent
'''

import numpy as np

def gauss(mat,vec):
    (n,p)=mat.shape
    for j in range(min(n,p)):
        i0=np.nonzero(mat[j:,j])[0][0]+j
        vec[[i0,j]]=vec[[j,i0]]
        mat[[i0,j],:]=mat[[j,i0],:]
        for k in range(j+1,n):
            piv=mat[k,j]/mat[j,j]
            mat[k,:]=mat[k,:]-piv*mat[j,:]
            vec[k]=vec[k]-piv*vec[j]
    #print(mat)
    #print(v)
    sol=[]
    for i in reversed(range(n)):
        nz=np.nonzero(mat[i,i:])[0]
        if nz.size==0:
            if vec[i]!=0:
                return "Pas de solution"
    return "Des solutions"
    

a=np.array([[1,3,5],[2,2,3],[2,0,4]],dtype=float)
v=np.array([1,2,3,4],dtype=float)

print(gauss(a,v))