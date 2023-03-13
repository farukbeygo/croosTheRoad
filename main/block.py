from turtle import Turtle
import random

# colors
COLORS = ["red", "blue", "orange", "purple", "pink", "green"]


class Block(Turtle):
    # constructor of the class
    def __init__(self):
        super().__init__()

        num_x = random.randint(300, 400)
        num_y = random.randint(-13, 13)

        self.shape("square")
        self.penup()
        self.goto(num_x, num_y * 20)
        self.color(random.choice(COLORS))
        self.left(180)
        self.shapesize(1, 2)





