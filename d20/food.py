from turtle import Turtle
from random import randint

width, height = 600, 600

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize_food()
        self.goto_random_position()

    def initialize_food(self):
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)

    def goto_random_position(self):
        self.goto(randint(-width / 2 + 30, width / 2 - 30), randint(-height / 2 + 20, height / 2 - 20))