#Ioannis Apomachos

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


#Initializing screen parameters
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


#Screen's keystrokes for navigating the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Check if the snake eats food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #Check collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Check collision with tail but avoiding the heads collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10: 
            game_is_on = False
            scoreboard.game_over()      

screen.exitonclick()