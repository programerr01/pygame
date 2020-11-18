from random import randrange 
from turtle import * 
import math
class vector:
    def __init__(self, x,y):
        self._hash = None
        self.x = x
        self.y = y

    def move(self, val):
        self.x += val.x
        self.y += val.y
    def copy(self):
        type_self = type(self)
        return type_self(self.x, self.y)
    def __repr__(self):
        type_self = type(self)
        name = type_self.__name__
        return '{}({!r}, {!r})'.format(name, self.x, self.y)
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __isub__(self, other):
        if self._hash is not None:
            raise ValueError('cannot subtract vector after hashing')
        if isinstance(other, vector):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

    def __sub__(self, other):
        copy = self.copy()
        return copy.__isub__(other)

def dist(a,b):
    return math.sqrt(abs(a.x-b.x)- abs(b.y-a.y))

ball = vector(-200,-200)
speed = vector(0,0)
targets = []

def tap(x,y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x+200)/25
        speed.y = (y+200)/25

def inside(xy):
    "Return True if xy within screen"
    return -200 < xy.x < 200 and -200 < xy.y <200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20,'blue')

    if(inside(ball)):
        goto(ball.x , ball.y)
        dot(10,'red')
    
    update()

def move():
    "Move ball and targets"
    if randrange(40) == 0:
        y = randrange(-150,150)
        target= vector(200,y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.25
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target-ball) > 24:
            targets.append(target)

    draw()
    for target in targets:
        if not inside(target):
            return 
    ontimer(move, 50)

setup(420,420,370,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()