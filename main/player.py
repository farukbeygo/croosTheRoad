from turtle import Turtle

INITIAL_X = 0
INITIAL_Y = -280
SPEED = 20


class Player(Turtle):
    # constructor of the class
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(INITIAL_X, INITIAL_Y)
        self.left(90)

    def move(self):
        """
        this method moves the turtle with determined speed
        :return:
        """
        self.forward(SPEED)

    def collide(self, block):
        """
        this method detect any collision of turtle and block
        :param block:
        :return:
        """
        if abs(block.xcor() - self.xcor()) < 30 and abs(block.ycor() - self.ycor()) < 20:
            return True

    def passed(self):
        """
        this method reset the position of the turtle
        :return:
        """
        self.goto(INITIAL_X, INITIAL_Y)