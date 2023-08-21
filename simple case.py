from turtle import *
from math import *

def cercle(R):
    hideturtle()
    up()
    color('black')
    goto(0,-10*R)
    down()
    circle(10*R)

def loup(x,y):
    L.up()
    L.goto(x,y)
    L.color('red')
    L.down()
    L.dot(3)

def canard(x,y):
    C.up()
    C.goto(x,y)
    C.color('green')
    C.down()
    C.dot(3)
#programme principal
cercle(10)
cercle(2.5)
L=Turtle()
C=Turtle()
loup(100,0)
canard(0,0)
t=0 
while t<10:
    t=t+0.1
    loup(100*cos(0.4*t),100*sin(0.4*t))
    canard(5*t*sqrt(2),-5*t*sqrt(2))
done()