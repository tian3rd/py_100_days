from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

"""
Snake class
"""

class Snake:
    def __init__(self, num_of_snakes=3):
        self.num_of_snakes = num_of_snakes
        self.is_moving = True
        self.snakes = []
        self.initialize()
    
    def initialize(self):
        for i in range(self.num_of_snakes):
            snake = self.new_snake()
            snake.goto(i * -20, 0)
            self.snakes.append(snake)
    
    def new_snake(self):
        snake = Turtle()
        snake.shape('square')
        snake.color('white')
        snake.penup()
        return snake

    def grow_snake(self):
        snake = self.new_snake()
        x_diff = self.snakes[-1].xcor() - self.snakes[-2].xcor()
        y_diff = self.snakes[-1].ycor() - self.snakes[-2].ycor()
        snake.goto(self.snakes[-1].xcor() + x_diff, self.snakes[-1].ycor() + y_diff)
        self.snakes.append(snake)
        self.num_of_snakes += 1
    
    def move(self):
        if self.is_moving:
            for i in range(self.num_of_snakes - 1, 0, -1):
                self.snakes[i].goto(self.snakes[i-1].xcor(), self.snakes[i-1].ycor())
            self.snakes[0].forward(20)
    
    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)
    
    def toggle_move(self):
        self.is_moving = not self.is_moving
