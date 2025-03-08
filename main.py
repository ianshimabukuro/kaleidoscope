import turtle as t
from itertools import cycle
import random

colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size,angle,shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size+random.randint(0,45), angle+random.randint(0,90),shift+random.randint(0,30))

t.bgcolor('black')
t.speed('fast')
t.pensize(4)

draw_circle(2,30,0)