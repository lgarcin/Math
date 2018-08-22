a = 1 + 1j
u = 1
for _ in range(10):
    u = (u + a / u) * .5
print(u, u ** 2, a)

from numpy.random import uniform
from numpy import eye
from numpy.linalg import inv, norm

A = uniform(-5, 5, (5, 5))
A = A.T.dot(A)
print(A)
U = eye(5)
for _ in range(10):
    U = (U + inv(U).dot(A)) * .5
print(norm(U.dot(U) - A))
