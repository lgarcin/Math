from numpy import linspace, meshgrid, sin, cos, exp
from matplotlib.pyplot import plot, show, figure
from random import gauss, random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def f(x, y):
    return exp(sin(x) * cos(y)) / (x ** 2 + y ** 2 + 10)
    # return sin(x)*sin(10*x)
    # return 10 * sin(.3 * x * sin(1.3 * x ** 2 + .00001 * x ** 4 + 0.2 * x + 80))


# X = linspace(-10, 10, 1000)
# Y = [f(x) for x in X]
# figure()
# plot(X, Y)
# show()

T = .1
x = 4
y = 4
e = f(x, y)
print(e)
lx = [x]
ly = [y]
le = [e]
while T > .001:
    xx = x + gauss(0, 1)
    yy = y + gauss(0, 1)
    ee = f(xx, yy)
    p = exp((ee - e) / T)
    if random() < p:
        x = xx
        y = yy
        e = ee
    T *= .999
    lx.append(x)
    ly.append(y)
    le.append(e)

figure()
plot(lx, ly)
figure()
plot(le)

ax = Axes3D(figure())
X, Y = meshgrid(linspace(-10, 10, 100), linspace(-10, 10, 100))
Z = f(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)
print(x, y, e)
show()
