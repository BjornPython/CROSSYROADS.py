from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.ht()
        self.penup()
        self.goto(0, 250)
        self.write(f"SCORE: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        """Updates the score"""
        self.clear()
        self.write(f"SCORE: {self.score}", align=ALIGN, font=FONT)

    def add_score(self):
        """Adds a score"""
        self.score += 1
        self.update_score()

    def game_over(self):
        """Called when the game is over"""
        self.clear()
        self.goto(0, 0)  # Go to middle of the screen
        self.write(f"GAME OVER\nYOUR SCORE IS: {self.score}", align="center", font=FONT)
