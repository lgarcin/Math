'''
Created on 3 juin 2012

@author: Laurent
'''

import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid

digits = load_digits()
n_components = .95
n_samples = len(digits.images)
pca = PCA(n_components=n_components)

perm = np.random.permutation(n_samples)
n = 500

train_images = digits.images[perm[:n]]
train_targets = digits.target[perm[:n]]
n_train = len(train_images)

test_images = digits.images[perm[n:]]
test_targets = digits.target[perm[n:]]
n_tests = len(test_images)

train = train_images.reshape((n_train, -1))
pca.fit(train)
train_pca = pca.transform(train)
    
test = test_images.reshape((n_tests, -1))
test_pca = pca.transform(test)

neigh = KNeighborsClassifier(n_neighbors=1, p=2, warn_on_equidistant=False)
#neigh=NearestCentroid()

neigh.fit(train, train_targets)
print "Sans ACP :", np.count_nonzero(neigh.predict(test) - test_targets), n_tests

neigh.fit(train_pca, train_targets)
print "Avec ACP :", np.count_nonzero(neigh.predict(test_pca) - test_targets), n_tests
