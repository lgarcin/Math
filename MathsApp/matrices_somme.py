from numpy import sum, array, zeros
from numpy.random import randint


def constraint(m):
    lignes = sum(m, axis=0)
    lignes = lignes[1:] - lignes[:-1]
    colonnes = sum(m, axis=1)
    colonnes = colonnes[1:] - colonnes[:-1]
    return (lignes == 0).all() and (colonnes == 0).all()


def binary(x, N):
    l = []
    for _ in range(N):
        l.append(x % 2)
        x //= 2
    return l


def solve(n, p):
    res = zeros((n + 1, p + 1), dtype=int)
    for k in range(2 ** (n * p)):
        mat = array(binary(k, n * p)).reshape(n, p)
        if constraint(mat):
            res[sum(mat[:, 0]), sum(mat[0, :])] += 1
    return res


n, p = 3, 6
print(solve(n, p))
