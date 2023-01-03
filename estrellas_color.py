import turtle
import random

def dibujar_estrella(t, x, y, color):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.color(color)
  t.begin_fill()
  for i in range(5):
    t.forward(20)
    t.right(144)
  t.end_fill()

def dibujar_galaxia(t, n):
  for i in range(n):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    color = (random.random(), random.random(), random.random())
    dibujar_estrella(t, x, y, color)

t = turtle.Turtle()
t.speed("fastest")
dibujar_galaxia(t, 50)
turtle.done()
