'''
Created on 3 juin 2012

@author: Laurent
'''

import pylab as pl
import numpy as np
from sklearn.datasets import fetch_olivetti_faces
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestCentroid
from scipy.stats import norm

faces = fetch_olivetti_faces()
n_components = 10
n_samples = len(faces.images)
pca = PCA(n_components=n_components)

ind = np.mod(range(40), 10) == 0

train_images = faces.images[np.negative(ind)]
train_targets = faces.target[np.negative(ind)]
n_train = len(train_images)

test_images = faces.images[ind]
test_targets = faces.target[ind]
n_tests = len(test_images)
for test in test_images:
    test = test + norm.rvs(scale=10, size=test.shape)
    for i in range(25, 30):
        test[i, :] = 0
        test[:, i] = 0
    test = np.minimum(test, 1)
    test = np.maximum(test, 0)
    test = np.zeros(test.shape)

train = train_images.reshape((n_train, -1))
train_pca = pca.fit_transform(train)
    
test = test_images.reshape((n_tests, -1))
test_pca = pca.transform(test)

neigh = NearestCentroid()

neigh.fit(train, train_targets)
print "Sans ACP :", np.count_nonzero(neigh.predict(test) - test_targets), n_tests

neigh.fit(train_pca, train_targets)
print "Avec ACP :", np.count_nonzero(neigh.predict(test_pca) - test_targets), n_tests

