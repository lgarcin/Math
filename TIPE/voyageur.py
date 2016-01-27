from itertools import combinations, permutations
from random import sample, random, randint
from math import exp, sqrt
from matplotlib.pyplot import plot, show, figure, axis


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# villes = ["Paris", "Lyon", "Marseille", "Tombouctou", "Bangkok"]
villes = list(range(20))
locations = {ville: (randint(-10, 10), randint(-10, 10)) for ville in villes}
distances = {pair: distance(locations[pair[0]], locations[pair[1]]) for pair in combinations(villes, 2)}


def longueur(chemin):
    l = 0
    n = len(chemin)
    for k in range(n):
        if (chemin[k], chemin[(k + 1) % n]) in distances:
            l += distances[chemin[k], chemin[(k + 1) % n]]
        else:
            l += distances[chemin[(k + 1) % n], chemin[k]]
    return l


T = 50
c = villes.copy()
l = longueur(c)
n = len(villes)
li = [l]
while T > .001:
    i, j = sample(range(n), 2)
    c[i], c[j] = c[j], c[i]
    ll = longueur(c)
    if random() > exp((l - ll) / T):
        c[i], c[j] = c[j], c[i]
    else:
        l = ll
    li.append(l)
    T *= .9999
# print(min([longueur(c) for c in permutations(villes)]))
print(c, longueur(c))

chemin = c + [c[0]]
figure()
axis([-11, 11, -11, 11])
plot([locations[ville][0] for ville in chemin], [locations[ville][1] for ville in chemin], marker='.')
figure()
plot(li)
show()
