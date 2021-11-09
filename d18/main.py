from turtle import Turtle, Screen
import turtle
from random import choice, randrange

def random_color_hex(): 
    random_number = randrange(0, 2**24)
    # need to add 0s when there are not enough 6 hex digits!!
    return "#"+hex(random_number)[2:] 

def random_color(): 
    r = randrange(2**8)
    g = randrange(2**8)
    b = randrange(2**8)
    
    return (r, g, b)

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
radius = 150
num_circles = 10

for i in range(num_circles): 
    tim.right(360/num_circles)
    
    color = random_color()
    tim.color(color)
    tim.circle(radius)


turtle.done()

