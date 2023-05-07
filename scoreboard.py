from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.max_score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 180)
        self.write(f"Player 1: {self.l_score}", align="center", font=("Courier", 30, "normal"))
        self.goto(200, 180)
        self.write(f"Player 2: {self.r_score}", align="center", font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def declare_winner(self):

        if self.l_score == self.max_score:
            self.clear()
            self.goto(0, 150)
            self.write(f"Player 1: {self.l_score}\nPlayer 2: {self.r_score}\n Player 2 has won!", align="center",
                       font=("Courier", 30, "normal"))
            return False

        if self.r_score == self.max_score:
            self.clear()
            self.goto(0, 150)
            self.write(f"Player 1: {self.l_score}\nPlayer 2: {self.r_score}\n Player 1 has won!", align="center",
                       font=("Courier", 30, "normal"))
            return False
