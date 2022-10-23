from turtle import Turtle
import random

ALIGNMENT = "Center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        self.score_total = -1
        self.goto(0, 280)
        self.hideturtle()
        self.score()

    def score(self):
        self.score_total += 1
        display_text = "Scores: " + str(self.score_total)
        self.clear()
        self.write(display_text, move=False, align=ALIGNMENT, font=('Arial', 8, 'bold'))

    def game_over(self, reason):
        if reason == 1:
            display_text = "GAME OVER! Hit the wall."
        else:
            display_text = "GAME OVER! Hit the tail."
        self.color("red")
        self.home()
        self.write(display_text, move=False, align="center", font=('Arial', 12, 'bold'))
