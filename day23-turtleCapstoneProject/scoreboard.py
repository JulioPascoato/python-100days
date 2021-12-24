from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-350, 260)
        self.write(f"Level: {self.level}", font=("Monospace", 15, "normal"))

    def level_up(self):
        self.level += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Monospace", 15, "normal"))

