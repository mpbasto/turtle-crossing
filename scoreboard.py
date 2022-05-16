from turtle import Turtle
from tkinter import messagebox

# Constants
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    """
    Creates a scoreboard object.
    """

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 255)
        self.update_scores()

    def update_scores(self):
        """
        Updates and displays scoreboard on the screen.
        """
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def level_up(self):
        """
        Increments level by 1.
        """
        self.level += 1
        self.update_scores()






