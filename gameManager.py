import time
from turtle import Screen
from tkinter import messagebox
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class GameManager:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen_setup()
        self.scores = Scoreboard()
        self.cars = CarManager()
        self.player = Player()
        self.controls(self.player)
        self.game_loop(self.player, self.cars, self.scores)

    def screen_setup(self):
        self.screen.clear()
        self.screen.title('Turtle Crossing')
        self.screen.tracer(0)
        self.screen.listen()

    def controls(self, player):
        self.screen.onkeypress(player.move, 'Up')
        self.screen.onkey(self.new_game, 'space')

    def new_game(self):
        response = messagebox.askquestion('New Game',
                                          'Would you like to start a new game?')
        if response == 'yes':
            self.__init__()
            self.screen_setup()
            self.controls()
            self.game_loop(self.player, self.cars, self.scores)

        elif response == 'no':
            messagebox.showinfo('Goodbye', 'Ok then! I\'ll see you soon.')
            self.screen.bye()
        else:
            messagebox.showwarning('Error', 'Something went wrong!')


    def game_over(self):
        response = messagebox.askquestion('GAME OVER', f'GAME OVER!\n\n Congrats, you manage to reach level {self.scores.level}!\n\n Would you like to start again?')

        if response == 'yes':
            self.__init__()
            self.screen_setup()
            self.controls()
            self.game_loop(self.player, self.cars, self.scores)

        elif response == 'no':
            messagebox.showinfo('Goodbye', 'Ok then! I\'ll see you soon.')
            self.screen.bye()
        else:
            messagebox.showwarning('Error', 'Something went wrong!')


    def game_loop(self, player, cars, score):

        game_is_on = True
        while game_is_on:
            time.sleep(0.1)
            self.screen.update()
            cars.move_cars()


            # Detect successful crossing
            if player.at_finish_line():
                score.level_up()
                cars.speed_up()
                cars.increment_threshold()


            # Detect collision with car
            for car in cars.all_cars:
                if car.distance(player) < 20:
                    self.game_over()
                    game_is_on = False

            cars.generate_new_car()

