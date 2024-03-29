# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 08:34:08 2022

@author: marisbotero
"""

import turtle
import random
turtle.bgcolor("darkblue")
turtle.speed(0)
turtle.hideturtle()

def ursamajor(i,j):
    
    for k in range(7):
        lst=["red","green","orange", "yellow","darkgray","brown","lightgreen"]
        turtle.color(lst[random.randint(0,6)])
        turtle.forward(i)           
        turtle.right(j)               

x=-350
y=-50
coordinates=((x,y),(x+135,y+1),(x+220,y-50),(x+330,y-105),(x+344,y-188), (x+470,y-209), (x+500,y-123))

def starconnect():
    for i in range(1):
        ursamajor(12,144)

for i in coordinates:
    turtle.penup()
    turtle.setpos(i)
    turtle.pendown()
    starconnect()

my=turtle.Turtle()
my.hideturtle()
my.penup()

for i in coordinates:
    my.goto(i)
    my.color("yellow")
    my.pendown()
my.goto(coordinates[-4])

turtle.exitonclick()