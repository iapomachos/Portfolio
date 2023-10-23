#Ioannis Apomachos

from turtle import Turtle,Screen
import random

my_screen = Screen()
my_screen.setup(width=500,height=400)
user_bet=my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False

colors = ["red", "orange", "yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
turtle_list = []

for index in range(0,6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colors[index])
    my_turtle.penup()
    my_turtle.goto(x=-230,y=y_positions[index])
    turtle_list.append(my_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in turtle_list:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



my_screen.exitonclick()