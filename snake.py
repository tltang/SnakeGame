import turtle as t
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        iy = 0
        for i in range(3):
            iy = iy - 20
            new_snake = t.Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.speed("fastest")
            new_snake.goto(x=0 + iy, y=0)
            self.snakes.append(new_snake)

    def move_forward(self):
        for segment in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[segment - 1].xcor()
            new_y = self.snakes[segment - 1].ycor()
            self.snakes[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        new_snake = t.Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.speed("fastest")
        new_snake.goto(self.snakes[-1].position())
        self.snakes.append(new_snake)
