from numpy import linspace
from matplotlib.pyplot import scatter, show


def f(r, x):
    return r * x * (1 - x)


def feigenbaum(r1, r2, nb):
    r_range = linspace(r1, r2, nb)
    x = []
    y = []
    for r in r_range:
        u = .1
        for _ in range(100):
            u = f(r, u)
        for _ in range(100):
            u = f(r, u)
            x.append(r)
            y.append(u)
    scatter(x, y, marker='.')
    show()


feigenbaum(3.5, 3.7, 1000)

# Parler de la nature fractale
