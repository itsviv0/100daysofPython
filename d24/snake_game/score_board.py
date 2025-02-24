from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
    
    def start_scoreboard(self):
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)    

    def update_scoreboard(self):
        self.clear()
        self.start_scoreboard()
        self.score += 1
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def read_file(self):
        with open('data.txt') as file:
            self.high_score = int(file.read())
    
    def write_file(self):
        with open('data.txt', mode='w') as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        self.update_scoreboard()
