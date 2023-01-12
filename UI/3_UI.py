from turtle import *
from random import randint
speed(0)
bgcolor("black")
x = 1
y = 11
while(x + y < 1400):
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    colormode(255)
    pencolor(red, green, blue)
    fd(30 + x)
    rt(90.911)
    x +=1
    y +=1

exitonclick()
