# -*- coding: utf-8 -*-
import turtle

# Función para dibujar una estrella
def draw_star(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(5, "white")

# Configurar la ventana
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Constelación de Pegaso")

# Configurar la tortuga
pegaso = turtle.Turtle()
pegaso.speed(0)  # velocidad máxima

# Coordenadas de las estrellas en la constelación de Pegaso (no son precisas)
estrellas = [
    (0, 0),    # Alpheratz
    (60, 40),  # Scheat
    (100, 0),  # Markab
    (60, -40), # Algenib
    (20, -20), # Enif
]

# Dibujar las estrellas
for x, y in estrellas:
    draw_star(pegaso, x, y)

# Dibujar las líneas entre las estrellas
pegaso.color("white")
pegaso.penup()
pegaso.goto(estrellas[0])  # Iniciar desde la primera estrella
pegaso.pendown()

for x, y in estrellas[1:]:  # Dibujar líneas a las otras estrellas
    pegaso.goto(x, y)

# Volver a la primera estrella para cerrar el cuadrilátero
pegaso.goto(estrellas[0])

# Dibujar la línea hacia Enif
pegaso.goto(estrellas[4])

# Esconder la tortuga y mostrar el dibujo
pegaso.hideturtle()
wn.mainloop()
