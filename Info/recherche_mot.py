'''
Created on 14 juil. 2013

@author: Laurent
'''

def recherche_mot(phrase,mot):
    n=len(phrase)
    m=len(mot)
    for i in range(n-m):
        test=True
        for j in range(m):
            if phrase[i+j]!=mot[j]:
                test=False
                break
        if test:
            return i
    return None

print(recherche_mot("Comment allez-vous ?","allez"))
