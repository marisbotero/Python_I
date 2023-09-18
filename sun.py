# -*- coding: utf-8 -*-
import turtle

# Configuración inicial
wn = turtle.Screen()
wn.bgcolor("black")  # Establecer el color de fondo a negro

luna = turtle.Turtle()
luna.speed(0)  # Dibujo más rápido

# Dibujar el círculo completo (luna llena)
luna.color("white")
luna.penup()
luna.goto(0, -50)
luna.pendown()
luna.begin_fill()
luna.circle(50)
luna.end_fill()

# Superponer un círculo para crear la fase de la luna menguante
luna.color("black")
luna.penup()
luna.goto(20, -50)
luna.pendown()
luna.begin_fill()
luna.circle(50)
luna.end_fill()

# Esconder el objeto turtle y mostrar el dibujo
luna.hideturtle()

# Mantener la ventana abierta
turtle.done()
