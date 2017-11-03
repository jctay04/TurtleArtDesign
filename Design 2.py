import turtle
from MyShape import *
turtle.colormode(255)
turtle.bgcolor("red")
turtle.tracer()

bob=turtle.Turtle()
bob.speed(0)

background(bob, 50)
move(bob, 0, 0)


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

for times in range(35):
    move(bob,0,0)
    bob.width(12)
    bob.color(0 , 255 - times, 0)
    bob.circle(200)
    bob.right(55)
