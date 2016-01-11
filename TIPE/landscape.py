from numpy import zeros, meshgrid, roll, concatenate
from numpy.random import normal
from matplotlib import cm
from matplotlib.pyplot import matshow, show, figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
from pprint import pprint

n = 6
a = zeros((2 ** n, 2 ** n))
loc = 0
scale = .1
size = 2 ** n

while size > 1:
    sub = a[::size, ::size]
    shape = sub.shape
    noise = normal(loc, scale, shape)
    a[size / 2::size, size / 2::size] = (sub + roll(sub, -1, 0) + roll(sub, -1, 1) + roll(roll(sub, -1, 0), -1,
                                                                                          1)) / 4 + noise
    # print(size)
    # pprint(a)

    sub1 = a[::size, ::size]
    sub2 = a[size / 2::size, size / 2::size]
    noise = normal(loc, scale, shape)
    a[size / 2::size, ::size] = (sub1 + roll(sub1, -1, 0) + sub2 + roll(sub2, 1, 1)) / 4 + noise
    noise = normal(loc, scale, shape)
    a[::size, size / 2::size] = (sub1 + roll(sub1, -1, 1) + sub2 + roll(sub2, 1, 0)) / 4 + noise
    # pprint(a)
    size //= 2
    scale /= 2

a = concatenate((a, a), axis=0)
a = concatenate((a, a), axis=1)
matshow(a,cmap=cm.gray)
show()
# x, y = meshgrid(range(0, a.shape[0]), range(0, a.shape[1]))
# ax = Axes3D(figure())
# ax.plot_surface(x, y, a, rstride=1, cstride=1, cmap=cm.jet, linewidth=1, antialiased=True)
show()
