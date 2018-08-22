from pulp import LpVariable, LpInteger, LpProblem, LpMaximize, lpSum, LpStatus, value
from math import gcd
from numpy import zeros


def solve(n, p):
    prob = LpProblem("routage", LpMaximize)
    matrix = LpVariable.dicts("Matrix", (range(n), range(p)), 0, 1, LpInteger)
    for i in range(n - 1):
        prob += lpSum(matrix[i][j] for j in range(p)) == lpSum(matrix[i + 1][j] for j in range(p))
    for j in range(p - 1):
        prob += lpSum(matrix[i][j] for i in range(n)) == lpSum(matrix[i][j + 1] for i in range(n))

    res = zeros((n + 1, p + 1), dtype=int)
    while True:
        prob.solve()
        if prob.status == 1:
            nl = int(sum([value(matrix[0][j]) for j in range(p)]))
            nc = int(sum([value(matrix[i][0]) for i in range(n)]))
            res[nc, nl] += 1
            prob += lpSum(matrix[i][j] for i in range(n) for j in range(p) if value(matrix[i][j]) == 1) + lpSum(
                1 - matrix[i][j] for i in range(n) for j in range(p) if value(matrix[i][j]) == 0) <= n * p - 1
        else:
            break
    return res


print(solve(4, 4))
