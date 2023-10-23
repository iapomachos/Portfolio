#Ioannis Apomachos

import turtle as turtle_module
import random

def random_color():
    """This method generates a random rgb color"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

turtle_module.colormode(255)
my_turtle = turtle_module.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
my_turtle.speed("fastest")
my_turtle.penup()


number_of_dots=100
random_color()

for dot_count in range(1, number_of_dots + 1):
    my_turtle.dot(20, random_color())
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()