from random import randint
def square( t, distance ):
    for times in range(4):
        t.forward(distance)
        t.left(4)

def triangle( t, distance ):
    for times in range(3):
        t.forward(distance)
        t.left(120)

def pentagon( t, distance ):
    for times in range(5):
        t.forward(distance)
        t.left(angle)

def circle(t):
    for times in range(100):
        t.forward(times * 3)
        t.right(times * 4)
        
def move(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def sprial(t, distance, side):
    angle=360/side
    for times in range(side):
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)
        t.color(red,green,blue)
        triangle(t, 40 - times)
        square(t, 40 - times)
        t.forward(6)
        t.left(5)

def dome(t, distance, side):
    angle = 360 / side
    for times in range(side):
        #red=randint(0,255)
        #green=randint(0,255)
        #blue=randint(0,255)
        t.color(255 - times, 100- times, 0)
        t.circle(distance)
        t.left(angle)

def polygon(t, distance, side):
    angle = 360 / side
    for times in range(side):
        t.forward(distance)
        t.left(angle)
        
def background(t, side):
    for times in range(side):
        t.begin_fill()
        square(t, 500)
        t.color(255 - times, 100 - times, 0)
        move(t, 0, 0)
        polygon(t, 100, 1)
        t.left(6)
        t.end_fill()
