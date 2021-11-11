from turtle import Turtle, Screen
from time import sleep

# customized packages
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# global variables 
width, height = 600, 600

screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor('black')
# turn animation off
screen.tracer(0)
num_of_snakes = 3

snakes = Snake(num_of_snakes)

food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snakes.up)
screen.onkey(key="Down", fun=snakes.down)
screen.onkey(key="Right", fun=snakes.right)
screen.onkey(key="Left", fun=snakes.left)
screen.onkey(key="t", fun=snakes.toggle_move)

is_game_on = True

while is_game_on:
    screen.update()
    sleep(0.1)

    snakes.move()

    # snake eats food (collision detection)
    if snakes.snakes[0].distance(food) < 15:
        snakes.grow_snake()
        food.goto_random_position()
        scoreboard.update_score()
    
    # snake hits the wall
    if abs(snakes.snakes[0].xcor()) > width/2 - 5 or abs(snakes.snakes[0].ycor()) > height/2 - 5:
        is_game_on = False
        scoreboard.show_gameover()

    # snake hits itself (collision detection)
    for snake in snakes.snakes[1:]:
        if snake.distance(snakes.snakes[0]) < 15:
            is_game_on = False
            scoreboard.show_gameover()
    
screen.exitonclick()
