from turtle import Turtle, Screen
from time import sleep

from snake import Snake

width, height = 600, 600
screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor('black')
screen.tracer(0)
num_of_snakes = 3

snakes = Snake(num_of_snakes)

screen.listen()
screen.onkey(key="Up", fun=snakes.up)
screen.onkey(key="Down", fun=snakes.down)
screen.onkey(key="Right", fun=snakes.right)
screen.onkey(key="Left", fun=snakes.left)

is_game_on = True

while is_game_on:
    screen.update()
    sleep(0.1)

    snakes.move()
    
screen.exitonclick()
