# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle
import random

# Configuración de la ventana
window = turtle.Screen()
window.bgcolor("black")
window.title("Galaxia de circulos bonitos")

# Creación de la tortuga para dibujar los circulos
cir = turtle.Turtle()
cir.speed(0)  # Configura la velocidad de la tortuga en su máximo valor (0)

# Función para dibujar un circulo
def draw_cir(size, color):
    cir.color(color)
    cir.begin_fill()
    cir.circle(size)
    cir.end_fill()

# Cantidad de circulos a dibujar
num_cirs = 50

# Dibuja cada circulo
for i in range(num_cirs):
    # Tamaño y color aleatorio para cada circulo
    size = random.randint(10, 50)
    color = (random.random(), random.random(), random.random())  # Genera un color RGB aleatorio

    # Posición aleatoria para cada circulo
    x = random.randint(-window.window_width()//2, window.window_width()//2)
    y = random.randint(-window.window_height()//2, window.window_height()//2)

    # Dibuja el circulo en la posición y con el tamaño y color aleatorio
    cir.penup()  # Levanta el lápiz de la tortuga para moverla sin dibujar
    cir.goto(x, y)
    cir.pendown()  # Baja el lápiz para dibujar
    draw_cir(size, color)

# Cierra la ventana al hacer clic en ella
window.exitonclick()
