from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CHANCE = 7
CARS_PROBABILITY_THRESHOLD = 2

# TODO: Create cars (height=20px, width=40px)
#   - randomly generated along the y-axis and move towards the left end of screen
#   - no cars should be generated in the top and bottom 50px of the screen (a safe zone for turtle)
#   - new cars are only generated every 6th time the game loop runs


class CarManager:
    """
    Randomly generates small rectangular objects (cars) along the y-axis
    and wil move them towards the left end of the screen. New cars are only generated every 6th time the game loop runs.

    - create_car(): creates a random car along the y-axis with a given dimension
    - move_cars():
    """

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.probability_threshold = CARS_PROBABILITY_THRESHOLD
        self.generate_initial_cars()
        self.starting_positions()

    def create_car(self):
        """
        Creates a random car along the y-axis with a given dimension.
        """

        new_car = Turtle('square')
        new_car.shapesize(stretch_wid= 1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-240, 240)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def generate_new_car(self):
        random_chance = random.randint(1, CHANCE)
        if random_chance < self.probability_threshold:
            self.create_car()
            self.all_cars[-1].goto(300, random.randrange(-240, 240, 20))

    def generate_initial_cars(self):
        nr_cars = random.randint(15, 30)
        for _ in range(nr_cars):
            self.create_car()
        print(f"Generated {len(self.all_cars)} starting cars.")

    def starting_positions(self):
        for car in self.all_cars:
            car.goto(random.randint(-260, 260), random.randrange(-240, 240, 20))

    def move_cars(self):
        """
        Goes through the car list (self.all_cars) and move each one towards the left by the constant STARTING_MOVE_DISTANCE.
        """
        for car in self.all_cars:
            car.backward(self.speed)

    def speed_up(self):
        """
        Increments speed of cars according to MOVE_INCREMENT constant.
        """
        self.speed += MOVE_INCREMENT

    def increment_threshold(self):
        self.probability_threshold += 1



