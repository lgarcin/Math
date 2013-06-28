'''
Created on 23 juin 2013

@author: Laurent
'''

import numpy as np

def Gauss(mat):
    n=len(mat)
    p=len(mat[0])
    for k in range(min(n,p)):
        ind=np.where
        mat[i], mat[k] = mat[k], mat[i]
        for j in range(k + 1, n):
            l = mat[j, k] / mat[k, k]
            mat[j] = [mat[j]]
        
