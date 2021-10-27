import sympy as sp


class Permutation(tuple):
    def __mul__(self, s):
        return Permutation(self[x] for x in s)


def sg(elts):
    a = {}
    b = set(elts)
    while a != b:
        a = set(b)
        b |= {s1*s2 for s1 in b for s2 in b}
    return b


print(sg({Permutation(x) for x in ((1, 2, 3, 0), (3, 2, 1, 0))}))

print(sg({sp.ImmutableMatrix(x)
              for x in (((1, 0), (0, -1)), ((0, -1), (1, 0)))}))
