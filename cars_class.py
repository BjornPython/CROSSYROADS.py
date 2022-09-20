from turtle import Turtle
import random

COLORS = ["blue", "yellow", "red", "green", "orange", "violet"]


class Cars:

    def __init__(self):
        self.all_cars = []  # A list to be iterated by a for loop to move the cars.
        self.car_speed = 10  # The speed of the cars.

    def make_car(self):
        make = random.randint(1, 6)
        if make == 1:
            new_car = Turtle("square")  # Shape of car
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch to make the square rectangular.
            new_car.penup()
            new_car.color(random.choice(COLORS))  # Randomly chooses a color
            new_car.goto(300, random.randint(-200, 300))  # Go to the car's starting position.
            self.all_cars.append(new_car)  # Append the car to the list.

    def move_cars(self):
        """Moves the cars in self.all_cars from right to left"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def collision(self, char):
        """Returns True if the character gets hit by the car"""
        for car in self.all_cars:
            if char.distance(car) < 15:
                return True
        return False

    def increase_diff(self):
        """Increases the difficulty by increasing the speed of the cars"""
        self.car_speed += 2
