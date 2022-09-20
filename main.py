import time
from turtle import Screen
from character_class import Character
from cars_class import Cars
from crossyroad_scoreboard_class import ScoreBoard

char = Character()
car = Cars()
screen = Screen()
score = ScoreBoard()
screen.setup(width=600, height=600)
screen.title("CROSSY ROADS beta")
screen.tracer(0)  # IMPORTANT
screen.listen()  # IMPORTANT
screen.onkey(char.move_up, "w")
screen.onkey(char.move_left, "a")
screen.onkey(char.move_right, "d")

game = True

while game:
    screen.update()
    time.sleep(0.1)
    car.make_car()
    car.move_cars()

    if char.ycor() >= 270:
        char.reset_pos()
        score.add_score()

    for c in car.all_cars:
        if char.distance(c) < 20:
            score.game_over()
            game = False

screen.exitonclick()
