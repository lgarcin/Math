from numpy import zeros, meshgrid, linspace, sin, cos, exp, sqrt, arange
from scipy.ndimage.filters import laplace
from matplotlib.pyplot import imshow, show, figure, axis, draw, contour
from matplotlib import cm
from math import pi
from mpl_toolkits.mplot3d import Axes3D


class Wave:
    def __init__(self, xmin, xmax, ymin, ymax, ds, dt, c, f, g):
        self.X, self.Y = meshgrid(arange(xmin, xmax, ds), arange(ymin, ymax, ds))
        self.ds = ds
        self.dt = dt
        self.c = c
        self.t = 0.
        self.previous = f(self.X, self.Y)
        self.boundary_conditions(self.previous)
        self.t += self.dt
        self.current = self.previous + g(self.X, self.Y) * self.dt
        self.boundary_conditions(self.current)

    def boundary_conditions(self, u):
        u[0, :] = u[-1, :] = u[:, 0] = u[:, -1] = 0
        w, h = u.shape
        if self.t <= 1000.:
            print(self.t)
            u[w // 2, h // 2] = .1 * sin(2 * pi / 30 * self.t)

    def update(self):
        self.t += self.dt
        self.current, self.previous = 2 * self.current - self.previous + laplace(self.current) * (
            self.c * self.dt / self.ds) ** 2, self.current
        # b = 1.
        # self.current, self.previous = (2 * self.current - (1 - b / 2 * self.dt) * self.previous + laplace(
        #     self.current) * (self.c * self.dt / self.ds) ** 2) / (1 + b / 2 * self.dt), self.current
        self.boundary_conditions(self.current)


class WaveImage(Wave):
    def __init__(self, xmin, xmax, ymin, ymax, ds, dt, c, f, g):
        super(WaveImage, self).__init__(xmin, xmax, ymin, ymax, ds, dt, c, f, g)
        self.fig = figure()
        self.img = imshow(self.current, cmap=cm.coolwarm, vmin=-.01, vmax=.01)

        self.timer = self.fig.canvas.new_timer(interval=10)
        self.timer.add_callback(self.update_plot)
        self.timer.start()

        show()

    def update_plot(self):
        self.update()
        self.img.set_data(self.current)
        draw()


class WaveContour(Wave):
    def __init__(self, xmin, xmax, ymin, ymax, ds, dt, c, f, g):
        super(WaveContour, self).__init__(xmin, xmax, ymin, ymax, ds, dt, c, f, g)
        self.fig = figure()
        self.p = contour(self.X, self.Y, self.current, [0])

        self.timer = self.fig.canvas.new_timer(interval=10)
        self.timer.add_callback(self.update_plot)
        self.timer.start()

        show()

    def update_plot(self):
        self.update()
        for col in self.p.collections:
            col.remove()
        self.p = contour(self.X, self.Y, self.current, [0])
        draw()


class Wave3D(Wave):
    def __init__(self, xmin, xmax, ymin, ymax, ds, dt, c, f, g):
        super(Wave3D, self).__init__(xmin, xmax, ymin, ymax, ds, dt, c, f, g)
        self.fig = figure()
        self.ax = Axes3D(self.fig)
        self.ax.set_zlim(-.5, .5)
        self.p = self.ax.plot_surface(self.X, self.Y, self.current, cmap=cm.coolwarm)

        self.timer = self.fig.canvas.new_timer(interval=10)
        self.timer.add_callback(self.update_plot)
        self.timer.start()

        show()

    def update_plot(self):
        self.update()
        self.ax.collections.remove(self.p)
        self.p = self.ax.plot_surface(self.X, self.Y, self.current, cmap=cm.coolwarm)
        draw()


def f(X, Y):
    return 0 * X
    n, m, a = 7, 11, .3
    Dx, Dy = 30, 30
    return .1 * sin(n * pi * X / Dx) * sin(m * pi * Y / Dy) + a * sin(m * pi * X / Dx) * sin(n * pi * Y / Dy)


def g(X, Y):
    u = 0 * X
    w, h = u.shape
    u[w // 2, h // 2] = 1.
    return u
    return 0 * X


wi = WaveImage(0, 30, 0, 30, .1, .1, .5, f, g)
# wc = WaveContour(0, 30, 0, 30, .1, .1, .5, f, g)
# w3 = Wave3D(0, 30, 0, 30, .5, 1, .05, f, g)
