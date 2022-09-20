from turtle import Turtle


class Character(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.setheading(90)  # To face the character North.
        self.goto(0, -260)  # Start at the starting position.

    def check_pos(self):
        """Returns True if the y coordinate of the character is more than 270"""
        if self.ycor() >= 270:
            self.reset_pos()
            return True

    def move_up(self):
        """Moves the character North"""
        self.forward(20)

    def move_left(self):
        """Moves the character West"""
        self.setheading(180)
        self.forward(20)
        self.setheading(90)

    def move_right(self):
        """Moves the character East"""
        self.setheading(0)
        self.forward(20)
        self.setheading(90)

    def reset_pos(self):
        """Resets the position if the Character"""
        self.goto(0, -260)
