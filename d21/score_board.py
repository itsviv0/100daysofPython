from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
    
    def start_scoreboard(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.start_scoreboard()
        self.score += 1
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)