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
        self.snakes = []
        self.initialize()
    
    def initialize(self):
        for i in range(self.num_of_snakes):
            snake = Turtle()
            snake.shape('square')
            snake.color('white')
            snake.penup()
            snake.goto(i * -20, 0)
            self.snakes.append(snake)
    
    def move(self):
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