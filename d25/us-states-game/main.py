import turtle
import pandas as pd
from PIL import Image
# import csv

screen = turtle.Screen()
screen.title("US States Game")
# gif image file name/path
us_map = 'blank_states_img.gif'
# read the size of image to set fit screen
image = Image.open(us_map)
width, height = image.size
screen.setup(width, height)
# background image
screen.bgpic(us_map)

states_df = pd.read_csv('50_states.csv')
states_lst = states_df['state'].tolist()

# store states in a dictionary for quick lookup
states = {state.upper(): (states_df[states_df['state'] == state].x.values[0],
                          states_df[states_df['state'] == state].y.values[0]) for state in states_lst}

NUM_STATES = 50
num_right_guesses = 0

turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")

guess = None
correct_guesses = []

while num_right_guesses < NUM_STATES:
    # if accidentally close the inputbox, re-open it
    while guess is None:
        guess = turtle.textinput(
            '{}/{} Guessed'.format(num_right_guesses, NUM_STATES), "Please guess a state: ")
    guess = guess.upper()
    # if user exits, generate a learning list
    if guess == 'EXIT':
        if num_right_guesses < NUM_STATES:
            print('You got {} out of {}'.format(num_right_guesses, NUM_STATES))
            states_to_learn = []
            for state in states.keys():
                if state not in correct_guesses:
                    states_to_learn.append(state)
            # with open('states_to_learn.csv', 'w') as f:
            #     writer = csv.writer(f)
            #     writer.writerow(states_to_learn)
            # alternatively use pandas to write to csv
            print(states_to_learn)
            states_to_learn_df = pd.DataFrame(states_to_learn)
            states_to_learn_df.columns = ['states_to_learn']
            states_to_learn_df.to_csv(
                f'{NUM_STATES - num_right_guesses} states to learn.csv', index=False)
        break
    if guess in states.keys():
        # display the state name on the map with corresponding coordinates
        turtle.goto(states[guess][0], states[guess][1])
        turtle.write(guess)
        num_right_guesses += 1
        correct_guesses.append(guess)
    # reset guess
    guess = None


screen.exitonclick()
