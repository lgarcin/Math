from matplotlib.pyplot import plot, legend, show
from math import sqrt
from numpy import logspace


def F(x, eps):
    u = 1
    v = x
    while abs(u - v) > eps:
        u, v = sqrt(u * v), (u + v) / 2
    return (u + v) / 2


x = logspace(-3, 1, 1000)
y = [F(t, 1e-3) for t in x]
plot(x, y, label=r"$F$")
y = [sqrt(t) for t in x]
plot(x, y, label=r"$x\mapsto\sqrt{x}$")
y = [(1 + t) / 2 for t in x]
plot(x, y, label=r"$x\mapsto\frac{1+x}{2}$")
legend()
show()

from matplotlib2tikz import save as tikz_save

tikz_save('test.tex')
