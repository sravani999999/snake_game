from turtle import Turtle

FONT=('Courier', 22, 'normal')
ALIGNMENT='center'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score=0
        self.hideturtle()
        self.penup()
        self.goto(40, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(50,0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)


    def increase(self):
        self.clear()
        self.score+=1
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

