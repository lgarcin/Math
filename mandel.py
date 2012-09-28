# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:31:12 2012

@author: Laurent
"""

from numpy import linspace, mgrid, zeros, copy, multiply, add, uint8, cos, sin
from PIL import Image, ImageOps

def mandel(n, m, itermax, xmin, xmax, ymin, ymax):
    ix, iy = mgrid[0:n, 0:m]
    x = linspace(xmin, xmax, n)[ix]
    y = linspace(ymin, ymax, m)[iy]
    c = x + complex(0, 1) * y
    del x, y
    img = zeros(c.shape, dtype=uint8)
    ix.shape = n * m
    iy.shape = n * m
    c.shape = n * m
    z = copy(c)
    for i in xrange(itermax):
        if not len(z): break
        multiply(z, z, z)
        add(z, c, z)
        rem = abs(z) > 2.0
        img[ix[rem], iy[rem]] = i + 1
        rem = -rem
        z = z[rem]
        ix, iy = ix[rem], iy[rem]
        c = c[rem]
    return img

if __name__ == '__main__':
    I = mandel(800, 800, 200, -2, .5, -1.25, 1.25)
    I[I == 0] = 201
    im = Image.fromarray(I)
    palette = []
    for i in range(256):
        palette.extend((int(127 * sin(i / 10) + 128), i, int(127 * cos(i / 10) + 128)))
    im.putpalette(palette)
    im = ImageOps.equalize(im)
    im.show()
