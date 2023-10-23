#Ioannis Apomachos

from turtle import Turtle,Screen

my_turtle = Turtle()
my_screen = Screen()


def forward():
    my_turtle.forward(20)

def backward():
    my_turtle.backward(20)

def turn_left():
    new_heading=my_turtle.heading() + 10
    my_turtle.setheading(new_heading)

def turn_right():
    new_heading=my_turtle.heading() - 10
    my_turtle.setheading(new_heading)

def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

my_screen.listen()
my_screen.onkey(key="w", fun=forward)
my_screen.onkey(key="s", fun=backward)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()