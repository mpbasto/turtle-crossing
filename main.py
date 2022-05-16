import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

# Instantiate player & cars
steve = Player()
car_manager = CarManager()

# Keyboard Bindings
screen.listen()
screen.onkeypress(steve.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()



# TODO: Detect collision with a car and stop game when it occurs


# TODO: Detect when turtle reaches top end of screen (aka Finish Line)
#   - turtle must then return to the starting position
#   - speed of cars must increase
#   - think about creating an attribute and using the MOVE_INCREMENT to increase the car speed


# TODO: Scoreboard that keeps track of current level
#   - every time the turtle crosses successfully, level += 1
#   - when turtle hits a car => Game over to be displayed in the center of screen


screen.exitonclick()