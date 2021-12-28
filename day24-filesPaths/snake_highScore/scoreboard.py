from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.hideturtle()
        self.get_high_score("data.txt")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score("data.txt")

        self.score = 0
        self.update_scoreboard()

    def get_high_score(self, filename):
        with open(filename) as file:
            contents = file.read()
            self.high_score = int(contents)

    def update_high_score(self, filename):
        with open(filename, mode="w") as file:
            file.write(f"{self.high_score}")
