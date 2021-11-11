from turtle import Turtle

width, height = 600, 600

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, height / 2 - 20)
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Courier', 15, 'normal'))
    
    def update_score(self):
        self.score += 1
        self.show_score()

    def show_gameover(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!', align='center', font=('Courier', 25, 'bold'))
