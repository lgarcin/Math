'''
Created on 21 mai 2012

@author: Laurent
'''

from random import normalvariate, uniform
from visvis import solidSphere, Point, gca, Timer, use

def distance2(a, b):
    dx = a.translation.x - b.translation.x
    dy = a.translation.y - b.translation.y
    dz = a.translation.z - b.translation.z
    return dx * dx + dy * dy + dz * dz

def getClique(ball, partition):
    for p in partition:
        if ball in p:
            return p

def merge(l):
    pos = Point(0, 0, 0)
    vel = Point(0, 0, 0)
    s = 0
    for b in l:
        s = s + b.mass
        pos += b.mass * b.translation
        vel += b.mass * b.velocity
    rad = s ** (1. / 3)    
    ball = solidSphere(pos / s, (rad, rad, rad))
    ball.velocity = vel / s
    ball.mass = s
    ball.radius = rad
    return ball

ballList = []
n = 100
G = 100
dt = .1

dpos = 10
dvel = 5
rad = .5

for i in range(n):
    x = normalvariate(0, dpos)
    y = normalvariate(0, dpos)
    z = normalvariate(0, dpos)
    vx = uniform(-dvel, dvel)
    vy = uniform(-dvel, dvel)
    vz = uniform(-dvel, dvel)
    ball = solidSphere(translation=(x, y, z), scaling=(rad, rad, rad))
    ball.radius = rad
    ball.velocity = Point(vx, vy, vz)
    ball.mass = ball.radius ** 3
    ballList.append(ball)

axes = gca()
#axes.SetLimits(rangeZ=(-2, 3))

def onTimer(event):
    l = len(ballList)
    for b in ballList:
        b.translation += Point(b.velocity) * dt
    collisions = [set([b]) for b in ballList]
    copyList = list(ballList)
    for b1 in ballList:
        copyList.remove(b1)
        for b2 in copyList:
            d = distance2(b1, b2)
            c = G * d ** (-3. / 2) * dt
            b1.velocity += c * b2.mass * (b2.translation - b1.translation)
            b2.velocity += c * b1.mass * (b1.translation - b2.translation)
            if d < (b1.radius + b2.radius) ** 2:
                p1 = getClique(b1, collisions)
                p2 = getClique(b2, collisions)
                if p1 is not p2:
                    collisions.append(p1.union(p2))
                    collisions.remove(p1)
                    collisions.remove(p2)
    for c in collisions:
        if len(c) > 1:
            ballList.append(merge(c))
            for b in c:
                ballList.remove(b)
                b.Destroy()
    if l != len(ballList):
        print(len(ballList))
    axes.Draw()


timer = Timer(axes, 100, False)
timer.Bind(onTimer)
timer.Start()
app = use()
app.Run()
