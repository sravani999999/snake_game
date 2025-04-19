from turtle import Turtle

FONT=('Courier', 22, 'normal')
ALIGNMENT='right'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(50, 270)
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(50,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)


    def increase(self):
        self.clear()
        self.score+=1
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

