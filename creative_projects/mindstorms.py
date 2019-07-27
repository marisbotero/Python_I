import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('pink')
    brad = turtle.Turtle()
    brad.shape()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    window.exitonclick()

draw_square()