# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import turtle
# from turtle import Turtle, Screen
import random
import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()
my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")
# my_screen.onkey(key="c", fun=move_home)

lContinue = True
i1 = 0

while lContinue:
    my_screen.update()
    time.sleep(0.1)

    my_snake.move_forward()

    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.grow()

        my_scoreboard.score()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        lContinue = False
        my_scoreboard.game_over(1)

    i1 = 0
    for snake in my_snake.snakes[1:]:
        i1 += 1
        if my_snake.head.distance(snake) < 5:
            print("at segment:", i1)
            lContinue = False
            my_scoreboard.game_over(2)

my_screen.exitonclick()

# def move_backwards():
#     new_turtle.backward(5)
#
# def move_counterclock():
#     current_heading = new_turtle.heading() + 5
#     new_turtle.setheading(current_heading)
#
# def move_clock():
#     current_heading = new_turtle.heading() - 5
#     new_turtle.setheading(current_heading)
#
# def move_home():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()