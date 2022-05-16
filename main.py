import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from gameManager import GameManager



# Set up screen
screen = Screen()
screen.setup(width=600, height=600)



def game_loop():
    while True:
        game = GameManager()
        game.new_game()
        game.screen.exitonclick()


game_loop()