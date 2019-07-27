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
    

    angie = turtle.Turtle()
    angie.shape()
    angie.color('violet')
    angie.circle(100)
    window.exitonclick()

draw_square()