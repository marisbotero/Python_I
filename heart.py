# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import turtle
import random

# Crea una ventana y un objeto Turtle
window = turtle.Screen()
window.bgcolor('black')
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Lista de colores para los corazones
colors = ['red', 'white', 'pink', 'purple', 'blue']

# Función para dibujar un corazón en una posición aleatoria
def draw_heart(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.left(45)
    pen.forward(100)
    pen.circle(50, 180)
    pen.right(90)
    pen.circle(50, 180)
    pen.forward(100)
    pen.end_fill()

# Dibuja 50 corazones en posiciones aleatorias
for i in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    color = random.choice(colors)
    draw_heart(x, y, color)

# Cierra la ventana al hacer clic en ella
window.exitonclick()
