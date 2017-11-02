import turtle
from MyShape import *
turtle.colormode(255)
turtle.bgcolor("black")
turtle.tracer()

bob=turtle.Turtle()
bob.speed(0)

for times in range(606):
    bob.color(255, 69, 0)
    bob.width(6)
    bob.circle(300000)
    bob.right(25)

for times in range(35):
    bob.width(5)
    bob.color(255, times + 10, 0)
    bob.circle(150)
    bob.right(55)
    bob.circle(55555555)
    bob.left(25)

bob.color(128 - times, 255 - times, 0)
move(bob, 0, 0)
square(bob, 20)




