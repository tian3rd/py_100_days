from random import randint
from turtle import Turtle, Screen

width = 500
height = 400
colors = ['black', 'red', 'blue', 'brown', 'yellow', 'green',]
screen = Screen()
screen.setup(width=width, height=height)
turtles = []
winner = ''

def initialize_turtles():
    for c in range(len(colors)):
        t = Turtle()
        t.shape('turtle')
        t.color(colors[c])
        t.penup()
        t.goto(-width / 2 + 20, height * (-1 / 3 + 2 * c / (3 * (len(colors) - 1))))
        # t.pendown()
        turtles.append(t)

def make_bet():
    bet = ''
    while bet == '':
        bet = screen.textinput("Make your bet!", f"Which turtle is going to win?\n{'/'.join(colors)}")
    return bet

def reached_deadline(xcor):
    return xcor + 20 >= width / 2

def race(bet=None):
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            turtle.forward(randint(0, int(width/50)))
            if reached_deadline(turtle.xcor()):
                winner = str(turtle.fillcolor())
                print(f"We've got a winner! Little {winner} wins!")
                is_race_on = False
                if bet == winner:
                    print("Yeah! You win!")
                else:
                    if bet is None:
                        print("Enjoy the show!")
                    else:
                        print(f"Sorry. You bet on {bet} and lose.")
                break

initialize_turtles()
bet = make_bet()
race(bet)

# print(screen.getshapes())

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def move_clockwise():
#     tim.right(10)

# def move_counterclockwise():
#     tim.left(10)

# def clear_screen():
#     tim.reset()

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="a", fun=move_counterclockwise)

# screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
