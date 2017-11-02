import turtle
from MyShape import *
turtle.colormode(255)
turtle.bgcolor("red")
turtle.tracer()

bob=turtle.Turtle()
bob.speed(0)

background(bob, 50)
move(bob, 0, 0)
bob.width(20)
dome(bob, 100, 25)

