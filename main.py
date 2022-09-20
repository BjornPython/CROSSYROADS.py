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
    car.make_car()  # Makes the cars randomly
    car.move_cars()  # Moves the cars

    if char.check_pos():  # Checks if the character's position is enough to score.
        score.add_score()  # adds 1 to the score
        car.increase_diff()  # Increases the speed of the cars.

    for c in car.all_cars:  # Checks the distance of the character compared to all the cars.
        if char.distance(c) < 20:
            score.game_over()
            game = False

screen.exitonclick()
