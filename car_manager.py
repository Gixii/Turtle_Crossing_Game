from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            random_y = random.randint(-240, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move_car(self):
        for cars in self.all_cars:
            cars.backward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT





