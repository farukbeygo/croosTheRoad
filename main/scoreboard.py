from turtle import Turtle


class ScoreBoard(Turtle):
    # constructor of the class
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(f"Level {self.level}", font=("Arial", 15, "normal"))

    def update(self):
        """
        this method update scoreboard
        :return:
        """
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", font=("Arial", 15, "normal"))

    def game_over(self):
        """
        this method just print game over
        :return:
        """
        self.color("black")
        self.goto(-100, 0)
        self.write("GAME OVER!!", font=("Arial", 25, "normal"))
