'''
Created on 3 juin 2012

@author: Laurent
'''

import numpy as np
import pylab as pl
from sklearn.datasets import fetch_olivetti_faces
from sklearn.decomposition import PCA
from scipy.stats import norm

faces = fetch_olivetti_faces()
pca = PCA(n_components= -1)

pl.gray()

for target in range(10):
    data = faces.images[faces.target == target]
    test = data[0]
    test = test + norm.rvs(scale=.1, size=test.shape)
#    for i in range(25, 30):
#        test[i, :] = 0
#        test[:, i] = 0
    test = np.minimum(test, 1)
    test = np.maximum(test, 0)
    pl.subplot(5, 4, 2 * target + 1)
    pl.imshow(test)

    data = data[1:]
    pca.fit(data.reshape((data.shape[0], -1)))
    test_pca = pca.transform(test.reshape(-1,))
    result = pca.inverse_transform(test_pca)
    pl.subplot(5, 4, 2 * target + 2)
    pl.imshow(result.reshape(test.shape))

pl.show()
