from turtle import Turtle

# Constants
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
        self.at_start()

    def move(self):
        """
        Sets orientation of player to a 90-degree angle to move towards the finish line.
        """
        self.forward(MOVE_DISTANCE)

    def at_start(self):
        """
        Places player at starting position.
        """
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        """
        Returns True when player reaches the finish line. False while it does not.
        """
        if self.ycor() > FINISH_LINE_Y:
            self.at_start()
            return True
        else:
            return False
