from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_distance = 5

    def create(self):
        random_chance = random.randint(0,7)
        if random_chance == 5:
            car = Turtle("square")
            car.color("white")
            car.penup()
            car.goto(300, random.randint(-255, 255))
            car.resizemode("user")
            car.turtlesize(1, 2, None)
            car.color(COLORS[random.randint(0, 5)])
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def move_increase(self):
        self.move_distance += 5