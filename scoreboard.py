from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.display_score()

    def display_score(self):
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Arial", 30, "normal"))

    def reset_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 20, "normal"))
