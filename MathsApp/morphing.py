from numpy import linspace, zeros, array, meshgrid, ones, gradient
from numpy.linalg import norm
from scipy.interpolate import griddata
from numpy.random import uniform


def interpolate(I, v, dt):
    x, y = meshgrid(linspace(0, 1, I.shape[1]), linspace(0, 1, I.shape[0]))
    vx, vy = v
    return griddata(
        ((x + vx * dt).flatten(), (y + vy * dt).flatten()),
        I.flatten(),
        (x, y),
        method='cubic')


class Morphing():
    def __init__(self, I0, I1, N):
        t = linspace(0, 1, N + 1)
        self.N = N
        self.dt = 1 / N
        self.I = array([(1 - tt) * I0 + tt * I1 for tt in t])
        self.v = array([zeros((2, *I0.shape)) for _ in range(N)])
        self.materialDerivative()

    def materialDerivative(self):
        self.materialDerivative = array(
            [interpolate(self.I[k + 1], self.v[k], self.dt) - self.I[k] for k in range(self.N)])

    def energyDeformation(self):
        return norm(self.v) ** 2 * self.dt

    def energyImage(self):
        return norm(self.materialDerivative) ** 2 * self.dt

    def energy(self):
        return self.energyDeformation() + self.energyImage()

    def gradientDeformation(self):
        pass


I0 = zeros((10, 10))
I1 = ones((10, 10))
morph = Morphing(I0, I1, 1)
print(morph.energy())
