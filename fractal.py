import turtle

def draw_triangle(some_turtle):
    for i in range(3):
        some_turtle.forward(50)
        some_turtle.left(120)
        some_turtle.begin_fill()
        for j in range(3):
            some_turtle.forward(25)
            some_turtle.left(120)
        some_turtle.end_fill()

def draw_art():
    brad = turtle.Turtle(shape="arrow")
    brad.color("black")
    brad.speed("fastest")
    for d in range(3):
        brad.left(120)
        for c in range(4):
            draw_triangle(brad)
            brad.forward(50)

    brad.hideturtle()

window = turtle.Screen()
window.bgcolor("white")
draw_art()
window.exitonclick()