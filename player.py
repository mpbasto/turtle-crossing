from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Creates player object in the shape of a turtle.
    - .move(): sets orientation of player to a 90-degree angle to move towards the finish line
    """

    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        """Sets orientation of player to a 90-degree angle to move towards the finish line."""
        self.forward(MOVE_DISTANCE)

