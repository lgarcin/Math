from pulp import LpVariable, LpInteger, LpProblem, LpMaximize, lpSum, LpStatus, value
from math import gcd

for s in range(1, 17):
    for d in range(1, 17):
        prob = LpProblem("routage", LpMaximize)
        matrix = LpVariable.dicts("Matrix", (range(s), range(d)), 0, 1, LpInteger)
        prob += lpSum(matrix[i][j] for i in range(s) for j in range(d)), "Maximiser"
        prob += lpSum(matrix[i][j] for i in range(s) for j in range(d)) >= 1
        prob += lpSum(matrix[i][j] for i in range(s) for j in range(d)) <= 32
        for i in range(s - 1):
            prob += lpSum(matrix[i][j] for j in range(d)) == lpSum(matrix[i + 1][j] for j in range(d))
        for j in range(d - 1):
            prob += lpSum(matrix[i][j] for i in range(s)) == lpSum(matrix[i][j + 1] for i in range(s))

        sol = prob.solve()
        print(LpStatus[sol], s, d, s * d / gcd(s, d))
        print(sum([value(matrix[i][j]) for i in range(s) for j in range(d)]))
        # for i in range(s):
        #     print([value(matrix[i][j]) for j in range(d)])
