#Ioannis Apomachos

from turtle import Screen
from cars import Cars
from crossing_turtle import CrossingTurtle
from scoreboard import Scoreboard
import time

#Initializing screen parameters
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

#Initializing Objects
my_turtle = CrossingTurtle()
car_factory = Cars()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(my_turtle.go_up,"Up")



game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_factory.create_car()
    car_factory.move_cars()

    #Check for collision
    for car in car_factory.all_cars:
        if car.distance(my_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Change level on successful run
    if my_turtle.is_at_finish_line():
        my_turtle.go_to_start()
        car_factory.level_up()
        scoreboard.score_point()
    

screen.exitonclick()