from turtle import *
from math import *

def cercle(R):
    hideturtle()
    up()
    color('black')
    goto(0, -R)
    down()
    circle(R)

def loup(r,angle):
    L.up()
    L.goto(r * cos(angle), r * sin(angle))
    L.color('red')
    L.down()
    L.dot(3)

def canard(r, angle):
    C.up()
    C.goto(r * cos(angle), r * sin(angle))
    C.color('green')
    C.down()
    C.dot(3)

## -----------------------------------------

cercle(100)
cercle(24)
L=Turtle()
C=Turtle()
loup(100, 0)
canard(0, 0)
t = 0
rC, aC = 0, 0

# parametres
t1 = 2.4
h = 0.1
while rC < 100:
    t = t + h 
    loup(100, 0.4 * t)
    if t < t1:
        rC, aC= rC + 10 * h, pi
        canard(rC, aC)
    elif abs(aC - 0.4 * t) < pi:
        teta = 2 * pi / rC #vitesse angulaire du canard
        rC, aC = rC, aC - teta * h
        canard(rC, aC)
    else:
        rC, aC = rC + 10 *h, aC
        canard(rC, aC)
done()